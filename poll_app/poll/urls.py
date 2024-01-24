from django.urls import path
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('poll/', views.poll_view, name='poll'),
    path('index/', views.index_view, name='index'), 
    path('registration/', views.registration_view, name='registration'), 
    path('', RedirectView.as_view(url='login/')), 
]
