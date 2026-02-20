from django.urls import path
from AdminApp import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_category/', views.add_category, name='add_category'),
    path('view_category/', views.view_category, name='view_category'),
    path('save_category/', views.save_category, name='save_category'),
    path('edit_category/<int:category_id>', views.edit_category, name='edit_category'),
    path('update_category/<int:category_id>', views.update_category, name='update_category'),
    path('delete_category/<int:category_id>', views.delete_category, name='delete_category'),


    path('add_products/', views.add_products, name='add_products'),
    path('view_products/', views.view_products, name='view_products'),
    path('save_products/', views.save_products, name='save_products'),
    path('edit_products/<int:product_id>', views.edit_products, name='edit_products'),
    path('update_products/<int:product_id>', views.update_products, name='update_products'),
    path('delete_products/<int:product_id>', views.delete_products, name='delete_products'),

    path('admin_loginpage/',views.admin_loginpage,name='admin_loginpage'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('contact_data/',views.contact_data,name='contact_data'),

]