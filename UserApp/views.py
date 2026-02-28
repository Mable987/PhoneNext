from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib import messages
from AdminApp.models import *
from UserApp.models import ContactDb, RegistrationDb, CratDb


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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        obj = RegistrationDb(UserName=username,Email=email,Password=password,Confirm_Password=confirm_password)
        if RegistrationDb.objects.filter(UserName=username).exists():
            print("User already exists")
            return redirect('signup')
        elif RegistrationDb.objects.filter(Email=email).exists():
            print("User already exists")
            return redirect('signup')
        else:
            obj.save()
            messages.success(request,'Registration successful')
            return redirect('signin')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if RegistrationDb.objects.filter(UserName=username,Password=password).exists():
            request.session['username'] = username
            request.session['password'] = password
            return redirect('home')
        else:
            return redirect('signin')
    else:
        return redirect('signin')

def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect('home')
def cart(request):
    return render(request,'cart.html')
def add_to_cart(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        productname = request.POST.get('productname')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        totalprice = request.POST.get('totalprice')
        pro = ProductDb.objects.filter(ProductName=productname).first()
        img = pro.ProductImage if pro else None
        obj = CratDb(UserName=username,ProductName=productname,Quantity=quantity,Price=price,TotalPrice=totalprice,ProductImage=img)
        obj.save()
        return redirect('cart')
