from django.contrib import admin
from django.urls import path
from .views import service_list, facility_list, index, generate_qr_code
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('services/', service_list, name='service_list'),
    path('facilities/', facility_list, name='facility_list'),
    path('qrcode/', generate_qr_code, name='qrcode'),
]
