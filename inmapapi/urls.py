from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_api,name="index"),
    
]