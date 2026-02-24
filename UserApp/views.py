from django.shortcuts import render, redirect
from django.template.context_processors import request

from AdminApp.models import *
from UserApp.models import ContactDb, RegistrationDb


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
    related_products = ProductDb.objects.all()
    return render(request,'single_item.html',{'single_product':single_product,'categories':categories,'related_products':related_products})
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
def user_signin(request):
    return render(request,'signin.html')
def user_signup(request):
    return render(request,'signup.html')
def save_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        obj = RegistrationDb(UserName=name,Email=email,Password=password,Confirm_Password=confirm_password)
        if RegistrationDb.objects.filter(UserName=name).exists():
            print("User already exists")
            return redirect('user_signup')
        elif RegistrationDb.objects.filter(UserName=email).exists():
            print("User already exists")
            return redirect('user_signup')
        else:
            obj.save()
            return redirect('user_signin')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if RegistrationDb.objects.filter(UserName=username,Password=password).exists():
            request.session['username'] = username
            request.session['password'] = password
            return redirect('Home')
        else:
            return redirect('user_signin')
    else:
        return redirect('user_signin')

def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect('Home')
