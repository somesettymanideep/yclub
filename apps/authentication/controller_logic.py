from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework import status
from datetime import datetime,timezone
from .models import *
from apps.authentication .utillis import *

from django.contrib.auth import login
from apps.home.models import *

def mobial_otp_logic(request):
    context = {}
    try:
        post_data = request.POST
        phone = post_data.get('mobile')
        if not phone:
            return JsonResponse({'error': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.get(phone=phone, is_active=True)
        if user:
            otp = generate_otp()
            send_otp(phone, otp)
            user.otp = otp
            print('sending otp is :'+ otp)
            user.otp_timestamp = datetime.now()
            user.save()
            request.session['user_id'] = user.id
            return JsonResponse({'message': 'OTP Sent. Register Phone number successfully!', 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'User not found or inactive'}, status=status.HTTP_400_BAD_REQUEST)

    except Users.DoesNotExist:
        return JsonResponse({'error': 'Phone number does not exist'}, status=status.HTTP_404_NOT_FOUND)


def mobial_otp_verify_logic(request):
    context = {}
    try:
        user_id = request.session.get('user_id')
        otp = request.POST['otp']
            
        user = Users.objects.get(id=user_id,is_active=True)
        current_time = datetime.now(timezone.utc)
        time_difference = user.otp_timestamp - current_time
        if (time_difference.total_seconds()/60) < 1:
            return JsonResponse({'error': 'OTP expired. Request for resend otp !!'}, status=status.HTTP_400_BAD_REQUEST)
            
        if int(otp) == user.otp:
            user.otp = None
            user.save()
            login(request, user)
            if user.role == "admin": 
                return JsonResponse({'path': '/dashboard/'},status=status.HTTP_200_OK)
            else:
                return JsonResponse({'path': '/dashboard/'},status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': f'{e}'}, status=401)
    

def user_register(request):
    context = {}
    try:    
        country = request.POST.get('country')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        pan = request.POST.get('pan')

        if Users.objects.filter(email=email).exists() or Users.objects.filter(phone=phone_number).exists():
            return JsonResponse({'error': 'User with this email or phone number already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        username = email.replace('.', '').split('@')[0]
        user = Users.objects.create(
            username= username,
            phone=phone_number,
            email=email,
            pan_number=pan
        )
        user.save()
        return JsonResponse({'path': '/'},status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': f'{e}'}, status=401)