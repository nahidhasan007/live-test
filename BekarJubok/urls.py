from django.urls import path
from . import views

urlpatterns = [
    path('',views.navbar,name="navbar"),
    path('register/',views.register,name="Register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('search/',views.search,name="search_results"),
    
    
]
