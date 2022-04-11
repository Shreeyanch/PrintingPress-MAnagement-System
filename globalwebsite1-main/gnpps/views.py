from django.shortcuts import get_object_or_404, redirect, render
from .models import Image
from .models import services 
from .models import faq 
from .models import clien
from .models import order
from .models import distribution
from .models import paper
from .models import ink



# Create your views here.
    
def index(request):
    pics=Image.objects.all()
    service=services.objects.all()
    faqs=faq.objects.all()
   
    return render(request,"gnpps/index.html",{
    "pics":pics,
    "service":service,
    "faq":faqs,
    
    })

def press(request):
    client = clien.objects.all()
    order1 = order.objects.all()
    distribution1 = distribution.objects.all()
    context = {
        'client':client,
        'order':order1,
        'distribution':distribution1,
    }
    return render(request,"gnpps/press.html",context)

def inventory(request):
    paper1 = paper.objects.all()
    ink1 = ink.objects.all()
    
    context = {
        'paper':paper1,
        'ink':ink1,
        
    }
    return render(request,"gnpps/inventory.html",context)


def add(request):
    if request.method == "POST":
        
        client_id= request.POST.get('client_id')
        client_name= request.POST.get('client_name')
        client_address= request.POST.get('client_address')
        client_phone= request.POST.get('client_phone')


        

        client = clien (
            client_id= client_id,
            client_name= client_name,
            client_address=client_address,
            client_phone=client_phone,

            
        )
       
        
        client.save()

        return redirect('press')
    return render(request, "gnpps/press.html")

# order

def add1(request):
    if request.method == "POST":
        

        order_no = request.POST.get('order_no')
        date = request.POST.get('date')
        deadline = request.POST.get('deadline')
        client_id1 = request.POST.get('client_id1')

        order1 = order (
           

            order_no= order_no,
            date=date,
            deadline=deadline,
            client_id = client_id1

        )
        order1.save()

        return redirect('press')
    return render(request, "gnpps/press.html")


def add2(request):
    if request.method == "POST":
        
        address = request.POST.get('address')
        transportation = request.POST.get('transportation')
        distribution_id = request.POST.get('distribution_id')
        client_id = request.POST.get('client_id')

        distribution1 = distribution (
           

            address= address,
            transportation=transportation,
            distribution_id=distribution_id,
            client_id = client_id

        )
        distribution1.save()

        return redirect('press')
    return render(request, "gnpps/press.html")

def add3(request):
    if request.method == "POST":
        
        size= request.POST.get('size')
        thickness = request.POST.get('thickness')
        purchase_date = request.POST.get('purchase_date')
        quantity = request.POST.get('quantity')

        paper1 = paper (
           

            size= size,
            thickness=thickness,
            purchase_date=purchase_date,
            quantity= quantity
        )
        paper1.save()

        return redirect('inventory')
    return render(request, "gnpps/inventory.html")
    
def Edit(request):
    client = clien.objects.all()
    context = {
        'client':client,
    }
    return redirect(request,"gnpps/press.html",context)

def Edit1(request):
    order1 = order.objects.all()
    context = {
        'order':order1,
    }
    return redirect(request,"gnpps/press.html",context)

def Edit2(request):
    distribution1 = distribution.objects.all()
    context = {
        'distribution':distribution1,
    }
    return redirect(request,"gnpps/press.html",context)

def Edit3(request):
    paper1 = paper.objects.all()
    context = {
        'paper':paper1,
    }
    return redirect(request,"gnpps/inventory.html",context)

def Update(request,id):
    if request.method == "POST":
        client_id= request.POST.get('client_id')
        client_name= request.POST.get('client_name')
        client_address= request.POST.get('client_address')
        client_phone= request.POST.get('client_phone')

        client = clien (
            id = id,
            client_id= client_id,
            client_name= client_name,
            client_address=client_address,
            client_phone=client_phone
        )
        client.save()

        return redirect('press')
    return redirect(request,"gnpps/press.html")

def Update1(request,id):
    if request.method == "POST":
        order_no = request.POST.get('order_no')
        date = request.POST.get('date')
        deadline = request.POST.get('deadline')
        client_id1 = request.POST.get('client_id1')

        order1 = order (
           

            order_no= order_no,
            date=date,
            deadline=deadline,
            client_id = client_id1

        )
        order1.save()
        

        return redirect('press')
    return redirect(request,"gnpps/press.html")



def Update2(request,id):
    if request.method == "POST":
        address = request.POST.get('address')
        transportation = request.POST.get('transportation')
        distribution_id = request.POST.get('distribution_id')
        client_id2 = request.POST.get('client_id2')

        distribution1 = distribution (
           

            address= address,
            transportation=transportation,
            distribution_id=distribution_id,
            client_id = client_id2

        )
        distribution1.save()
        

        return redirect('press')
    return redirect(request,"gnpps/press.html")

def Update3(request,id):
    if request.method == "POST":
        

        size= request.POST.get('size')
        thickness = request.POST.get('thickness')
        purchase_date = request.POST.get('purchase_date')
        quantity = request.POST.get('quantity')

        paper1 = paper (
            size= size,
            thickness=thickness,
            purchase_date=purchase_date,
            quantity = quantity
        )

        paper1.save()
        

        return redirect('inventory')
    return redirect(request,"gnpps/inventory.html")

def Delete(request,id):
    client=clien.objects.filter(id=id)
    client.delete()
    context = {
        'client':client,
    }
    return redirect('press')




def Delete1(request,id):
    order1=order.objects.filter(id=id)
    order1.delete()
    context = {
        'order':order1,
    }
    return redirect('press')


def Delete2(request,id):

    distribution1 = distribution.objects.filter(id=id)
    context = {
        'distribution':distribution1,
    }
    
    distribution1.delete()
   
    return redirect('press')

def Delete3(request,id):

    paper1 = paper.objects.filter(id=id)
    context = {
        'paper':paper1,
    }
    
    paper1.delete()
   
    return redirect('inventory')
# login
# from django.contrib.auth.models import User,auth
# from django.contrib import messages

def login(request):
    return render(request,"gnpps/login.html")

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        

        if username=='shreeyanch' and password=='purPlemango0':
            return redirect('press')
        else:
            
            return redirect('index')
    else:
        return render(request,'Login.html')