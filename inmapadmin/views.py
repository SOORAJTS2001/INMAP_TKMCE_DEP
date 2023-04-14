from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render, redirect
from inmap_cred.models import ApiAccounts


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
    #show  all the Api accounts in the html page
    api_accounts = ApiAccounts.objects.all()
    return render(request, 'inmapadmin/inmap_admin.html', {'api_accounts': api_accounts})
