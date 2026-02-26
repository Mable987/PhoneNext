from django.urls import path
from UserApp import views
urlpatterns = [
    path('home/',views.Home,name='home'),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('services/',views.services,name='services'),
    path('contacts/',views.contact_page,name='contacts'),
    path('save_contacts',views.save_contacts,name='save_contacts'),
    path('filtered_products/<str:cat_name>/', views.filtered_products, name='filtered_products'),
    path('single_product/<int:product_id>/', views.single_product, name='single_product'),
    path('signin/',views.user_signin,name='signin'),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('save_signup/',views.save_signup,name='save_signup'),


]