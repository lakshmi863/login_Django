
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage route
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),   # Signup page route
 
]
