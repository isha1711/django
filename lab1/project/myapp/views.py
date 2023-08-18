from django.shortcuts import render
from .models import Register 

# Create your views here.
def register(request):
	if request.method=='POST':
		fname=request.POST.get("fname")
		lname=request.POST.get("lname")
		email=request.POST.get("email")
		Pas=request.POST.get("Pas")
		cpas=request.POST.get("cpas")

		if Pas==cpas:

			query=Register(fname=fname,lname=lname,email=email,Pas=Pas,cpas=cpas)
			query.save()
			return render(request,'login.html')
		else:

			pass
	return render(request,'signup.html')

def login(request):
	if request.method == "POST":
		fname=request.POST.get("fname")
		Pas=request.POST.get("Pas")
		checkuser=Register.objects.filter(fname=fname,Pas=Pas)
		if checkuser:
			request.session['fname']=fname
			return render(request, 'index.html' ,{'name':fname})


		else:
			pass
	return render(request,'login.html')

def index(request):
	return render(request,'index.html')