from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('index/', views.index_view, name='index'), 
    path('', views.registration_view, name='registration'), 
]
