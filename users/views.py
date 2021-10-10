from django.shortcuts import  render, redirect
from .forms import NewUserForm, User
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import get_user_model

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return render(request=request, template_name="users/dashboard.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="users/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			print(user)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard.html")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="users/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("users/dashboard.html")
def dashboard(request):
#  if request.user.is_authenticated:
 	User = get_user_model()
 	users = User.objects.all()
 	return render(request, "users/dashboard.html",{'users':users})
#  else:
# 	 return redirect("users/login.html")

def edit(request, id):  
 user = User.objects.get(id=id)  
 return render(request,'users/edit.html', {'user':user})

def update(request, id):  
 user = User.objects.get(id=id)  
 form = NewUserForm(request.POST, instance = user)  
 if form.is_valid():  
  form.save()
  print("valid")  
  return redirect("/dashboard.html")  
 return render(request, 'users/edit.html', {'user': user})  
def destroy(request, id):  
 user = User.objects.get(id=id)  
 user.delete()  
 return redirect("/")