from django.urls import path

from . import views

app_name = "patchistiks"
urlpatterns = [
    path('', views.home, name="home"),
]