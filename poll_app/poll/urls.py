from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index_view, name='index'), 
    # Add login URL similarly
]
