from django.shortcuts import render, redirect, get_list_or_404
from django.http.response import HttpResponseRedirect
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .instantiate import save_models_to_database
from .models import MarkerModel


def download_marker_data_and_save(request):
    save_models_to_database()
    return render(request, 'marker_app/downloaded.html')

def display_marker_data(request):
    context = {}

    marker_list = get_list_or_404(MarkerModel)

    context['marker_list'] = marker_list

    return render(request, 'marker_app/data.html', context)






class MarkersView(APIView):
    def get(self, request, *args, **kw):
        marker_list = get_list_or_404(MarkerModel)
        markers = serializers.serialize('json', marker_list)
        return Response(markers, status=status.HTTP_200_OK)
