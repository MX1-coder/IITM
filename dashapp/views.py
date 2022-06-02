from django.shortcuts import render,redirect
# from django import template
from django.contrib.auth.decorators import login_required 
from .models import Product,Employee
from .forms import ProductForm,EmployeeForm
from django.http import HttpResponseRedirect,HttpResponse

from django.shortcuts import get_object_or_404
#orderview
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, QueryDict
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from .models import Product
from .forms import ProductForm
from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
# from auth.utils import form_validation_error
from django.core.exceptions import ValidationError     
from django.db.models import Sum ,Count,Max          
# Create your views here.

@login_required(login_url="/login/")
def index(request):
    items = Order.objects.all()
    total_price = sum(items.values_list('price', flat=True))
    maxp = Order.objects.all()
    max_price = max(maxp.values_list('price',flat=True))
    # items =Order.objects.aggregate(Sum('price'))
    products=Product.objects.all()
    orders=Order.objects.all()
    count= Order.objects.all().count()
    countp=Product.objects.all().count()
    context={'products':products,'orders':orders,'count':count,'sum':sum,'items':total_price,'countp':countp,'max_price':max_price}
    return render(request,'home/index.html',context)

@login_required(login_url="/login/")
def userprofile(request):
    return render(request,'home/page-user.html')

@login_required(login_url="/login/")
def editproduct(request,id):
    context = Product.objects.get(id = id)
    return render(request,'home/editproduct.html', {'context':context})

def createproduct(request):
    upload = ProductForm()
    if request.method == 'POST':
        upload = ProductForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('showproduct')
        else:
            return HttpResponseRedirect("""your form is wrong, reload on <a href = "{{ url : 'createproduct'}}">reload</a>""")
    else:
        return render(request, 'home/createproduct.html', {'upload_form':upload})

@login_required(login_url="/login/")
def showproduct(request):
    context=Product.objects.all()
    return render(request,'home/showproduct.html',{'context':context})

@login_required(login_url="/login/")
def categoryshow(request):
    return render(request,'home/categoryshow.html')

@login_required(login_url="/login/")
def tablelist(request):
    return render(request,'home/ui-tables.html')

@login_required(login_url="/login/")
def typography(request):
    return render(request,'home/ui-typography.html')

@login_required(login_url="/login/")
def notifiactions(request):
    return render(request,'home/ui-notifications.html')


def update_product(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product); 
    if form.is_valid():  
        form.save()  
        return redirect("/showproduct")  
    return render(request, 'home/editproduct.html', {'context': product})

def delete_product(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return render(request,'home/showproduct.html')


# employee module

@login_required(login_url="/login/")
def createemployee(request):
    upload = EmployeeForm()
    if request.method == 'POST':
        upload = EmployeeForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/showemployee')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'createemployee'}}">reload</a>""")
    else:
        return render(request, 'home/createemployee.html', {'upload_form':upload})

@login_required(login_url="/login/")
def showemployee(request):
    context=Employee.objects.all()
    return render(request,'home/showemployee.html',{'context':context})

@login_required(login_url="/login/")
def editemployee(request,id):
    context = Employee.objects.get(id=id)
    return render(request,'home/editemployee.html', {'context':context})

@login_required(login_url="/login/")
def update_employee(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee); 
    if form.is_valid():  
        form.save()  
        return redirect("/showemployee")  
    return render(request, 'home/editmployee.html', {'context': employee})

@login_required(login_url="/login/")
def delete_employee(request,id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return render(request,'home/showemployee.html')


#---------------Orderviewa--------


@login_required(login_url="/login/")
def createorder(request):
    upload = OrderForm()
    if request.method == 'POST':
        upload = OrderForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/showorder')
        else:
            return redirect('/createorder',msg='you put the wrong')
    else:
        return render(request, 'home/createorder.html', {'upload_form':upload})

@login_required(login_url="/login/")
def showorder(request):
    context=Order.objects.all()
    return render(request,'home/showorder.html',{'context':context})

@login_required(login_url="/login/")
def editorder(request,id):
    context = Order.objects.get(id=id)
    return render(request,'home/editorder.html', {'context':context})

@login_required(login_url="/login/")
def update_order(request, id):  
    order = Order.objects.get(id=id)  
    form = OrderForm(request.POST, instance = order); 
    if form.is_valid():  
        form.save()  
        return redirect("/showorder")  
    return render(request, 'home/editorder.html', {'context': order})

@login_required(login_url="/login/")
def delete_order(request,id):  
    order = Order.objects.get(id=id)  
    order.delete()  
    return render(request,'home/showorder.html')








