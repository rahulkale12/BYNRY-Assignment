from django.shortcuts import render,redirect
from .models import Customer, ServiceRequest,SupportTeam
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils.decorators import method_decorator


## view for support team registration ##################

def register_support_team(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']

        if SupportTeam.objects.filter(email=email).exists():
            return render(request, 'register_support_team.html', {'error': 'Email already exists!'})

        try:
            support_team = SupportTeam(name=name, email=email, phone=phone, address=address, password=password)
            support_team.save()
            return redirect('/customer_service/login_support_team/')
        except IntegrityError:
            return render(request, 'register_support_team.html', {'error': 'An error occurred while registering. Please try again.'})

    return render(request, 'register_support_team.html')


## view for support team login #################################

def login_support_team(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            support_team = SupportTeam.objects.get(email=email, password=password)
            request.session['support_id']= support_team.id
            return render(request, 'manage_requests.html')
        except SupportTeam.DoesNotExist:
            return render(request, 'login_support_team.html',{'error':'Invalid Credentials'})
        
    return render(request,'login_support_team.html')


## view for support team logout #############################

def logout_support_team(request):
    request.session.flush()  
    return redirect('/customer_service/login_support_team/')


## decorator for support team as only logged in support team can access requests to resolve it #################

def login_support_team_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('support_id'):
            return redirect('/customer_service/login_support_team/') 
        return view_func(request, *args, **kwargs)
    return wrapper


@login_support_team_required
def resolve_request(request, request_id):
    try:
        service_request = ServiceRequest.objects.get(id=request_id)
    except ServiceRequest.DoesNotExist:
        return redirect('manage_requests') 

    if request.method == 'POST':
        service_request.status = 'Resolved'
        service_request.resolved_date = timezone.now()
        service_request.save()
        return redirect('manage_requests')

    return render(request, 'resolve_request.html', {'service_request': service_request})


## view to manage requests #######################

@login_support_team_required
def manage_requests(request):
    # service_requests = ServiceRequest.objects.filter(status='Pending')
    service_requests = ServiceRequest.objects.all()
    return render(request, 'manage_requests.html', {'service_requests': service_requests})


