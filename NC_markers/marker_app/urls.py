from django.conf.urls import url, include
from . import views

app_name = 'marker_app'

urlpatterns = [
    url(r'^download/$', views.download_marker_data_and_save, name='download')

    ]