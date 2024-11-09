from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.
# @login_required(login_url="/login/")
def index(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/dashboard.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))



def datatables(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/data-tables.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
# @login_required(login_url="/")
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
    
# @login_required(login_url="/")
def loans(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/loans.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
# @login_required(login_url="/")  
def invoices(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/invoice.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
# @login_required(login_url="/")
def profile(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/profile.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))

# @login_required(login_url="/")    
def contactbook(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/contactbook.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))

# @login_required(login_url="/")    
def cards(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/cards.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
# @login_required(login_url="/")
def payouts(request):
    context ={'segment': 'payouts'}
    try:
        html_template = loader.get_template('home/dashboard.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))

# @login_required(login_url="/")
def collect(request):
    context ={'segment': 'collect'}
    try:
        html_template = loader.get_template('home/collect.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
# @login_required(login_url="/")
def utility_payments(request):
    context ={'segment': 'utility_payments'}
    try:
        html_template = loader.get_template('home/utility_payments.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
# @login_required(login_url="/")
def merchant_device(request):
    context ={'segment': 'merchant_device'}
    try:
        html_template = loader.get_template('home/merchant_device.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))

# @login_required(login_url="/")
def settlements(request):
    context ={'segment': 'settlement'}
    try:
        html_template = loader.get_template('home/settlement/settlement.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    

# @login_required(login_url="/")
def statements(request):
    context ={'segment': 'statements'}
    try:
        html_template = loader.get_template('home/statements/statement.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))

# @login_required(login_url="/")
def contactbook(request):
    context ={'segment': 'contactbook'}
    try:
        html_template = loader.get_template('home/contactbook/contactbook.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))


def addinvoice(request):
    context ={'segment': 'addinvoice'}
    try:
        html_template = loader.get_template('home/addinvoice.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
def device(request):
    context ={'segment': 'device'}
    try:
        html_template = loader.get_template('home/fintechdevice.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
    
