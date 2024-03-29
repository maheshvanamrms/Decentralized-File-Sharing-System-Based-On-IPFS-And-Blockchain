from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.Registration.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('key-generation/', views.KeyGeneration.as_view()),
    path('upload/', views.Uploading.as_view()),
]