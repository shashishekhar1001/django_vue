from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.

def course(request):
    return render(request, 'test.html' , {}) 