from django.urls import path

from . import views

app_name = "patchistiks"
urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('login/', views.myLogin, name="login"),
    path('register/', views.register, name="register"),
]