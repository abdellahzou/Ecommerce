from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('Cart/',include('cart.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('order/', include('order.urls'),)




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
