from django.shortcuts import render
from django.http import HttpResponse
from home.models import student

def home(request):
    return render(request,"index.html")

def success(request):
    return HttpResponse("<h1>this is  my success page</h1>")

def saveData(request):
    n=''
    if request.method=="POST":
        category=request.POST.get('category')
        pname=request.POST.get('productName')
        sku=request.POST.get('sku')
        quantity=request.POST.get('quantity')
        en=student(category=category,pname=pname,sku=sku,quantity=quantity)
        en.save()
        n='Data Inserted successfully'
    return render(request,"index.html",{'n':n})