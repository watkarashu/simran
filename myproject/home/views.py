from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Home
from django.template import loader
from django.urls import reverse

# Create your views here.
def home(request):
    return HttpResponse('Hello')

def index(request):
    if request. method=='POST':
        name = request.POST.get('name')
        mobilenumber = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        area = request.POST.get('area')
        a=Home(name=name,mobilenumber=mobilenumber,email=email,area=area)
        a.save()
    return render(request,'index.html')

def show(request):
    myhome = Home.objects.all().values()
    template = loader.get_template('show.html')
    context={
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    myhome = Home.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))

def updaterecords(request,id):
    name=request.POST['name']
    mobilenumber=request.POST['mobilenumber']
    email=request.POST['email']
    area=request.POST['area']
    home=Home.objects.get(id=id)
    home.name=name
    home.mobilenumber=mobilenumber
    home.email=email
    home.area=area
    home.save()
    return HttpResponseRedirect(reverse('show'))