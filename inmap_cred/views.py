from django.shortcuts import render
from .models import ApiAccounts
import random,string
# Create your views here.
def create_account(request):
    if request.method == 'POST':
        # Retrieve the form data from the request object
        organization = request.POST['organization']
        institution = request.POST['institution']
        expected_requests = request.POST['expected-requests']
        api_cred = api_cred = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        api_secret = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
        apiaccounts = ApiAccounts.objects.create(organization=organization,institution=institution,api_cred=api_cred,api_secret=api_secret,expected_requests=expected_requests)
        apiaccounts.save()
        print("created account of api cred {api_cred} and api secret {api_secret}")
    
        return render(request,'inmap_cred/create_account.html',{'api_cred':api_cred,'api_secret':api_secret})
    else:
        # If the request method is not POST, just render the form template
        return render(request,'inmap_cred/create_account.html')
def change_account_api(request):
    if request.method == 'POST':
        # Retrieve the form data from the request object
        organization = request.POST['organization']
        institution = request.POST['institution']
        expected_requests = request.POST['expected-requests']
        api_cred = request.POST['api_cred']
        api_secret = request.POST['api_secret']
        apiaccounts = ApiAccounts.objects.create(organization=organization,institution=institution,api_cred=api_cred,api_secret=api_secret,expected_requests=expected_requests)
        apiaccounts.save()
        print("created account of api cred {api_cred} and api secret {api_secret}")
    
        return render(request,'inmap_cred/create_account.html',{'api_cred':api_cred,'api_secret':api_secret})
    else:
        # If the request method is not POST, just render the form template
        return render(request,'inmap_cred/create_account.html')
