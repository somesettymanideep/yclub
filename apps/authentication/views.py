from django import template
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your views here.
def otp_login(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('accounts/otp-login.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    

def otp_validate(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('accounts/otp-validate.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        password = request.POST.get('password')
       

        # Basic server-side validation
        if not (username and phone_number and email and city and state and zip_code and password):
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        # Try to create the user or handle any validation errors
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            # Optionally, add custom fields for city, state, zip, and phone number in the profile
            user.save()
            print(user)
            # Redirect path after successful registration
            return JsonResponse({'path': '/success/'}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred. Please try again later.'}, status=500)

    # For GET request, render the registration form
    context = {'segment': 'index'}
    try:
        html_template = loader.get_template('accounts/auth-register.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render({}, request))
    except Exception:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render({}, request))
    
@login_required
def dashtwo(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/main-dashboard.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
@login_required
def logout_view(request):
    context ={}
    try:
        logout(request)
        return redirect('/')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))