from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import get_object_or_404
from django.contrib import messages

from AdminApp.models import CategoryDb, ProductDb
from UserApp.models import ContactDb


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
def add_category(request):
    return render(request, 'add_category.html')
def view_category(request):
    categories = CategoryDb.objects.all()
    return render(request, 'view_category.html', {'categories': categories})
def save_category(request):
    if request.method == "POST":
        categoryname = request.POST.get('categoryname')
        description = request.POST.get('description')
        categoryimage = request.FILES.get('categoryimage')
        obj  = CategoryDb(CategoryName=categoryname, Description=description, CategoryImage=categoryimage)
        obj.save()
        messages.success(request, 'Category Added Successfully')
        return redirect(add_category)
def edit_category(request,category_id):
    data = CategoryDb.objects.get(id=category_id)
    return render(request, 'edit_category.html', {'data': data})
def update_category(request, category_id):
    data = CategoryDb.objects.get(id=category_id)

    if request.method == "POST":

        data.CategoryName = request.POST.get('categoryname')
        data.Description = request.POST.get('description')

        categoryimage = request.FILES.get('categoryimage')

        if categoryimage:
            data.CategoryImage = categoryimage
        data.save()
        return redirect('view_category')
    return render(request, 'edit_category.html', {'data': data})

def delete_category(request,category_id):
    category = CategoryDb.objects.filter(id=category_id)
    category.delete()
    return redirect(view_category)








def add_products(request):
    categories = CategoryDb.objects.all()
    return render(request, 'add_products.html', {'categories': categories})
def view_products(request):
    products = ProductDb.objects.all()
    return render(request, 'view_products.html', {'products': products})
def save_products(request):
    if request.method == "POST":
        categoryname = request.POST.get('categoryname')
        productname = request.POST.get('productname')
        description = request.POST.get('description')
        price = request.POST.get('price')
        productimage = request.FILES.get('productimage')
        obj = ProductDb(Category_Name=categoryname,ProductName=productname, Description=description, Price=price, ProductImage=productimage)
        obj.save()
        messages.success(request, 'Product Added Successfully')
        return redirect(add_products)
def edit_products(request,product_id):
    data = ProductDb.objects.get(id=product_id)
    categories = CategoryDb.objects.all()
    return render(request, 'edit_products.html', {'data': data, 'categories': categories})
def update_products(request,product_id):
    data = get_object_or_404(ProductDb, id=product_id)
    if request.method == "POST":
        data.Category_Name = request.POST.get('categoryname')
        data.ProductName = request.POST.get('productname')
        data.Description = request.POST.get('description')
        data.Price = request.POST.get('price')
        productimage = request.FILES.get('productimage')
        if productimage:
            data.ProductImage = productimage
        data.save()
        return redirect('view_products')
    return render(request, 'edit_products.html', {'data': data})
def delete_products(request,product_id):
    product = get_object_or_404(ProductDb, id=product_id)
    product.delete()
    return redirect('view_products')



def admin_loginpage(request):
    return render(request, 'admin_loginpage.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username__contains=username).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                request.session['password'] = password
                return redirect(dashboard)
            else:
                print("Incorrect username or password")
                return redirect(admin_loginpage)
        else:
            print("User does not exist")
            return redirect(admin_loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)
def contact_data(request):
    contacts = ContactDb.objects.all()
    return render(request, 'contact_data.html', {'contacts': contacts})
