from django.shortcuts import render
from .models import Service, Category, Facility, Background_Image, About
from io import BytesIO
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import qrcode
from django.http import HttpResponse

# Create your views here.

def service_list(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    return render(request, 'service.html', {'categories': categories, 'services': services})

def facility_list(request):
    facilities = Facility.objects.all()
    categories = Category.objects.all()
    return render(request, 'facility.html', {'facilities': facilities, 'categories': categories})

def generate_qr_code(request):
    menu_url = request.build_absolute_uri('/') + '/'
    qr=qrcode.make(menu_url)
    buffer=BytesIO()
    qr.save(buffer,format='PNG')
    buffer.seek(0)
    return HttpResponse(buffer,content_type='image/png')


def index(request):
    services = Service.objects.all()
    background_image = Background_Image.objects.all()
    about = About.objects.all()
    facilities = Facility.objects.all()
    categories = Category.objects.all()
    return render(request,'index.html',{'services':services,'background_image':background_image,'facilities':facilities,'categories':categories,'about':about })




