from django.urls import path
from cart.views import add_to_cart, cart, checkout, hx_menu_cart, update_cart, hx_cart_total, success
urlpatterns= [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='Add_to_Cart'),
    path('', cart, name='Cart'),
    path('Checkout/', checkout, name='Checkout'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart' ),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
    path('Success/', success, name='Success'),

]