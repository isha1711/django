from django.shortcuts import render
from .models import prodmodel

# Create your views here.
def index(request):
	return render(request, 'index.html')
def add(request):
	return render(request, 'add.html')
def display(request):
	return render(request, 'display.html')
def search(request):
	return render(request, 'search.html')
def saveproduct(request):
	PName=request.GET['PName']
	PBrand=request.GET['PBrand']
	PPrice=request.GET['PPrice']
	Stock=request.GET['Stock']
	p=prodmodel(PName=PName,PBrand=PBrand,PPrice=PPrice,Stock=Stock)
	p.save()
	data=prodmodel.objects.all()
	return render(request, 'display.html' , {'data':data})
def saveview(request):
	sname=request.GET['sname']
	data=prodmodel.objects.filter(PName__contains=sname)
	return render(request,'search.html',{'Data': data})