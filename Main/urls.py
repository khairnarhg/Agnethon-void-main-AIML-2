from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('home/', views.home),
    path('learn/', views.learn),
    path('about/', views.about),
    path('uploadvid/', views.uploadvid),
    path('uploadaud/', views.uploadaud),
    path('uploadimg/', views.uploadimg)
]