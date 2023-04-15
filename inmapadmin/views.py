from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render, redirect
from inmap_cred.models import ApiAccounts
from django.contrib import messages
from important_pts_tkmce.important_pts import api_img_path,web_img_path
import os
def get_directory_size(path='.'):
    total_size = 0
    total_cnt =0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
            total_cnt+=1
    return round(total_size/(1024*1024),2),total_cnt
def delete_files_in_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('data')
        else:
            return render(request, 'inmapadmin/admin_login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'inmapadmin/admin_login.html')
@login_required(login_url='/inmap-admin/login/')
def inmap_admin(request):
    
    api_size,api_cnt = get_directory_size(api_img_path)
    web_size,web_cnt = get_directory_size(web_img_path)
    #show  all the Api accounts in the html page
    if request.method == 'GET':
        if request.GET.get('delete-api'):
            print('delete-api')
            ApiAccounts.objects.all().delete()
            messages.success(request, 'All API accounts deleted successfully!')
        elif request.GET.get('delete-web-images'):
            delete_files_in_dir(web_img_path)
            web_size=0.0
            web_cnt=0
            messages.success(request, 'All Web images deleted successfully!')
        elif request.GET.get('delete-api-images'):
            delete_files_in_dir(api_img_path)
            api_size=0.0
            api_cnt=0
            messages.success(request, 'All API images deleted successfully!')

    api_accounts = ApiAccounts.objects.all()
    return render(request, 'inmapadmin/inmap_admin.html', {'api_accounts': api_accounts,'api_size':api_size,'web_size':web_size,'api_cnt':api_cnt,'web_cnt':web_cnt})
