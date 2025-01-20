from django.shortcuts import render,redirect
from .models import Customer
from customer_service.models import ServiceRequest

# Create your views here.

## view for cutomer registration #######################

def register_customer(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        customer = Customer(name=name, email=email, phone=phone, address=address, password=password)
        customer.save()
        return redirect('/customer/login_customer/')
    return render(request, 'customer_register.html')


### view for customer login ########################

def login_customer(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email, password=password)
            request.session['customer_id']= customer.id
            return redirect('view_account')
        except Customer.DoesNotExist:
            return render(request, 'customer_login.html',{'error':'Invalid Credentials'})
        
    return render(request,'customer_login.html')

## view for customer logout ###################

def logout_customer(request):
    request.session.flush()
    return redirect('/customer/login_customer/')


### View For Submitting the request ##############################

def submit_service_request(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login_customer')
    
    if request.method == 'POST':
        customer = Customer.objects.get(id=customer_id)  
        service_type = request.POST['service_type']
        details = request.POST['details']
        file_attachment = request.FILES.get('file_attachment')
        
        service_request = ServiceRequest.objects.create(
            customer=customer,
            service_type=service_type,
            details=details,
            file_attachment=file_attachment,
            status = "Pending"
        )
        
        return redirect('/track_request/')

    return render(request, 'submit_service_request.html')


### View For Tracking the request ############# 
def track_request(request):
    customer_id = request.session.get('customer_id')  
    if not customer_id:
        return redirect('/customer/login_customer/')  

    try:
        customer = Customer.objects.get(id=customer_id)
        service_requests = ServiceRequest.objects.filter(customer=customer) 
    except Customer.DoesNotExist:
        return redirect('/customer/login_customer/') 

    return render(request, 'track_request.html', {'service_requests': service_requests})


## view for account info ############################

def view_account(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('/customer/login_customer')
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return redirect('/customer/register_customer')
    return render(request, 'account_info.html', {'customer': customer})