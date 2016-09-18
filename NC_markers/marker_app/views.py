from django.shortcuts import render, redirect
from .instantiate import save_models_to_database
from django.http.response import HttpResponseRedirect
# Create your views here.

def download_marker_data_and_save(request):
    save_models_to_database()
    return HttpResponseRedirect('downloaded.html')
