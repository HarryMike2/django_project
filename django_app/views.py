from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
# Create your views here.
def home(request):
    context={}
    return render(request, 'django_app/index.html', context)

def create(request):
    images = Service_Photo.objects.all()

    if request.method == 'POST':
        if request.POST.get('customer_name') and request.POST.get('customer_name'):
            form = Customer()
            form.customer_name = request.POST.get('customer_name')
            form.customer_phoneNumber = request.POST.get('customer_phoneNumber')
            form.service_photo = request.POST.get('service_photo')
        if request.POST.get('service_photo'):
            form.zab_name = request.POST.get('service_photo')
            form.user = request.user
            form.save()
            messages.success(request, 'okay')
            return redirect('index')
        else:
 
            messages.info(request, 'somnthg want wrong')
            return redirect('create')
    else:
        form = Customer()
    return render(request, 'django_app/create.html', {'form':form,'images':images})

    