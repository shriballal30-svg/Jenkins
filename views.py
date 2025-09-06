
from django.shortcuts import render,redirect

from employe.models import Details

# Create your views here.
def home(request):
    return render(request,"employe/home.html")
def about(request):
    return render(request,"employe/about.html")
def ragistration(request):
    if request.method == "POST":
        
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        city=request.POST.get('city')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        data=Details(name=name,mobile=mobile,city=city,age=age,gender=gender)
        data.save()
    return render(request,"employe/ragistration.html")
def record(request):
    data=Details.objects.all()
    context={
        'data':data
    }
    return render(request,"employe/record.html",context)
def update(request,id):
    data=Details.objects.get(id=id)
    context={
        'data':data
    }
    if request.method=="POST":
        
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        city=request.POST.get('city')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

   
        data.name=name
        data.mobile=mobile
        data.city=city
        data.age=age
        data.gender=gender
        data.save()
    return render(request,"employe/update.html",
                  context)
def delete(request,id):
    data=Details.objects.get(id=id)
    data.delete()
    return redirect('/record/')