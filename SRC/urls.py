from django.contrib import admin
from django.urls import path

from .views import(
    course,
)
app_name = 'SRC'

urlpatterns = [
    path('', course, name='course'),
]