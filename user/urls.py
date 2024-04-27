from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.Login.as_view(),name='login'),
    path('logout/', views.logout,name='logout')
]