from django.shortcuts import render
from django.views.generic import ListView
from django.db import models
from date.models import Test
# Create your views here.

class MainPage(ListView):
    model = Test
    template_name = "date/main_area.html"