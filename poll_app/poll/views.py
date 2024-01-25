from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import UserProfile,SaveRecord



# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Create a UserProfile instance and save it to the database
#             user_profile = UserProfile(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 age=form.cleaned_data['age'],
#                 cnic=form.cleaned_data['cnic'],
#                 mobile_no=form.cleaned_data['mobile_no'],
#                 nationality=form.cleaned_data['nationality'],
#                 gender=form.cleaned_data['gender'],
#                 password=form.cleaned_data['password'],
#             )
#             user_profile.save()

#             # Redirect to the login page
#             return redirect('login')  # Assuming you have a login page with the name 'login'
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_profiles = UserProfile.objects.all()

        for user_profile in user_profiles:
            if email == user_profile.email and password == user_profile.password:
                messages.success(request, 'Login successful!')
                return redirect('index')

        messages.error(request, 'Incorrect email or password. Please try again.')

    return render(request, 'login.html')
def index_view(request):
    return render(request,'index.html')

def registration_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        cnic = request.POST.get('cnic')
        mobile_no = request.POST.get('mobile_no')
        nationality = request.POST.get('nationality')
        gender = request.POST.get('gender')
        password = request.POST.get('password')

        UserProfile.objects.create(
            name=name,
            email=email,
            age=age,
            cnic=cnic,
            mobile_no=mobile_no,
            nationality=nationality,
            gender=gender,
            password = password
        )
        return redirect('login')  
       
    return render(request,'registration.html')

def saveRecord(request):
    if request.method == 'POST':
        question = request.POST.get('questions')
        option = request.POST.get('option')

        SaveRecord.objects.create(
            question=question,
            option=option,
        )

        return redirect('poll')
    return render(request,'poll.html')

def poll_view(request):
    return render(request,'poll.html')