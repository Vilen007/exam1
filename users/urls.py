from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('home',views.home1, name="home1"),
    path('users',views.users, name="users"),
    path('details',views.details, name="details")

]
