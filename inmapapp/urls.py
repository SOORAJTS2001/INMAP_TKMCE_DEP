from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="index"),
    path('sample', views.sample,name="sample"),
    path('test', views.test,name="test"),
    path('result', views.result,name="result")
]