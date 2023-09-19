from django.urls import path 
from core.views import frontpage, shop, signup, myaccount, edit_myaccount
from django.contrib.auth import views
from product.views import product



urlpatterns = [
    path('Signup/', signup, name='Signup'),
    path('logout/', views.LogoutView.as_view(), name='Logout'),
    path('Login/', views.LoginView.as_view(template_name = 'core/login.html'), name='Login'),
    path('', frontpage, name='frontpage'),
    path('Shop/',shop, name='Shop'),
    path('Shop/<slug:slug>/',product, name='Product'), 
    path('Myaccount/', myaccount, name='Myaccount'),
    path('Myaccount/Edit', edit_myaccount, name='Edit_Myaccount'),
 
]