from django.shortcuts import render, redirect
from django.template.context_processors import request

from AdminApp.models import *
from UserApp.models import ContactDb


# Create your views here.
def Home(request):
    categories = CategoryDb.objects.all()
    latest_products = ProductDb.objects.all().order_by('-id')[:8]
    return render(request,'Home.html',{'categories':categories,'latest_products':latest_products})
def about(request):
    return render(request,'about.html')
def products(request):
    products = ProductDb.objects.all()
    categories = CategoryDb.objects.all()
    featured_products = ProductDb.objects.all().order_by('-id')[:3]
    return render(request,'products.html',{'products':products,'categories':categories,'featured_products':featured_products})
def services(request):
    return render(request,'services.html')
def contacts(request):
    return render(request,'contact_page.html')
def filtered_products(request,cat_name):
    featured_products = ProductDb.objects.all().order_by('-id')[:3]
    categories = CategoryDb.objects.all()
    products_filtered = ProductDb.objects.filter(Category_Name=cat_name)
    return render(request,'filtered_products.html',{'products_filtered':products_filtered,
                                                    'categories':categories,'featured_products':featured_products})
def single_product(request,product_id):
    single_product = ProductDb.objects.get(id=product_id)
    categories = CategoryDb.objects.all()
    return render(request,'single_item.html',{'single_product':single_product,'categories':categories})
def contact_page(request):
    return render(request,'contact_page.html')
def save_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactDb.objects.create(
                name=name,
                email=email,
                message=message
            )
            return redirect('contacts')
        else:
            return redirect('contacts')

