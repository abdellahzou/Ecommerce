from django.urls import path
from .views import start_order

urlpatterns = [
    path('Start_order/', start_order, name='Start_order'),


]