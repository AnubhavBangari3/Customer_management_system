from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.http import HttpResponse
from .models import Customer,Product,Order,Tag
from .forms import OrderForm,RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required






from django.forms import inlineformset_factory

from .filters import OrderFilter


def login_view(request):
    
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(User,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Not valid")
    else:
        return render(request,"Accounts/login.html")

def registerPage(request):
    
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            
            
            user=authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect(reverse('login'))
        else:
            pass
            
    else:
        
        form=RegisterForm()
        
    
    return render(request,"Accounts/register.html",{
            'form': form,
            
        })


    
 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))



def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_order=orders.count()
    delivered=orders.filter(status="Delivered").count()
    pending=orders.filter(status="Pending").count()
    context={
        'orders':orders,
        'customers':customers,
        'total_order':total_order,
        'delivered':delivered,
        'pending':pending
    }
    
    return render(request,"Accounts/dashboard.html",context)

def about(request):
    return HttpResponse("about")


def product(request):
    products=Product.objects.all()
    context={
        "products": products
    }
    return render(request,"Accounts/products.html",context)

def customer(request,pk):
    customer=Customer.objects.get(pk=pk)
    
    ##reverse relationship of Customer and Order shown in Order - customer
    orders=customer.customer.all()
    total_order=orders.count()
    
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs
    
    context={'customer':customer,
             'orders':orders,
             'total_order':total_order,
             'myFilter':myFilter
             }
    return render(request,"Accounts/customer.html",context)

def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=3)#parent model , chid model
    
    customer=Customer.objects.get(pk=pk)
    formSet=OrderFormSet(instance=customer)
    
    if request.method == 'POST':
        formSet=OrderForm(request.POST)
        if formSet.is_valid():
            formSet.save()
            return redirect('home')
        
        
    
    context={
        'formSet':formSet
        
             }
    return render(request,"Accounts/order_form.html",context)

def updateOrder(request,pk):
    
    order=Order.objects.get(pk=pk)
    form=OrderForm(instance=order)
    
    if request.method == 'POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
       
    
    
    context={
        'form':form
        
             }
    return render(request,"Accounts/update_form.html",context)

def deleterOrder(request,pk):
    order=Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    
    context={
        'order':order
        
             }
    return render(request,"Accounts/delete.html",context)
    
