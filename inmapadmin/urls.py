from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.admin_login,name="login"),
    path('data/', views.inmap_admin,name="data"),
    path('delete-images/',views.delete_by_worker,name="delete_by_worker")
    
]