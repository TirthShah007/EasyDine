from django.shortcuts import render, HttpResponse, redirect
from EasyDineApp.models import Booking
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'rest_owner/login.html')

def forgot_password(request):
    # Logic for handling forgot password
    return render(request, 'rest_owner/forgot_password.html')

def payment(request):
    return render(request, 'rest_owner/payment.html')

def dashboard(request):
    return render(request, 'rest_owner/dashboard.html')

def login(request):
    return render(request, 'rest_owner/login.html')

def feedback(request):
    return render(request, 'rest_owner/feedback.html')

def addrestaurant(request):
    return render(request, 'rest_owner/addrestaurant.html')

def editrestaurant(request):
    return render(request, 'rest_owner/editrestaurant.html')

def signup(request):
    return render(request, 'rest_owner/signup.html')

def dashboard(request):
    bookings =Booking.objects.order_by('-id') 
    return render(request, 'rest_owner/dashboard.html', {'bookings':bookings})
    

#add restaurant form subbmission on databse
from .models import Restaurant
# from .forms import RestaurantForm

def addrestaurant(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        post = request.POST['post']
        city = request.POST['city']
        about = request.POST['about']
        phone = request.POST['phone']
        image = request.FILES['upload']
        
        restaurant = Restaurant(
            name=name,
            address=address,
            post=post,
            city=city,
            about=about,
            phone=phone,
            image=image
        )
        
        restaurant.save()
        return redirect('dashboard.html')  # Redirect to a page where you display all restaurants
    
    return render(request, 'rest_owner/addrestaurant.html')

#login & signup 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import ownerSignUpForm

# Other view functions...

def owner_signup_view(request):
    if request.method == 'POST':
        form = ownerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user object
            login(request, user)  # Log in the user after registration
            return redirect('login.html')  # Redirect to dashboard or desired page after login
    else:
        form = ownerSignUpForm()
    return render(request, 'rest_owner/signup.html', {'form': form})

def owner_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('rest_owner/index.html')  # Redirect to dashboard or desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'rest_owner/login.html', {'form': form})

def owner_logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
