from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a UserProfile instance and save it to the database
            user_profile = UserProfile(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                age=form.cleaned_data['age'],
                cnic=form.cleaned_data['cnic'],
                mobile_no=form.cleaned_data['mobile_no'],
                nationality=form.cleaned_data['nationality'],
                gender=form.cleaned_data['gender'],
                password=form.cleaned_data['password'],
            )
            user_profile.save()

            # Redirect to the login page
            return redirect('login')  # Assuming you have a login page with the name 'login'
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if the entered email and password are correct
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in and redirect to the index page
            login(request, user)
            return redirect('index')  # Replace 'index' with the name of your index page
        else:
            # Display an error message if email and password are incorrect
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')  # Replace 'login.html' with the actual login template path