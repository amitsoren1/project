from django.contrib import admin
from django.urls import path,include
from .views import Api

urlpatterns = [
    path("api",Api.as_view()),
]