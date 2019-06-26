from django.shortcuts import render,redirect
from crudapplication.forms import EmployeeForm
from crudapplication.models import Employee

from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
# Create your views here.

def emp(request):
    if request.method == "POST":
        form= EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,"index.html",{"form":form})

def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {"employees": employees})

def edit(request,id):
    empolyee= Employee.objects.get(id=id)
    return render(request,"edit.html",{"employee":empolyee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form =  EmployeeForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"edit.html",{'employee':employee})

def delete():
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def search( request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match= Employee.objects.filter(
                                         Q(eid__iexact=srch)|
                                         Q(ename__istartswith=srch)|
                                         Q(email__icontains=srch)
                                         )

            if match:
                return render(request,'search.html',{'sr' : match})
            else:
                messages.error(request,'No Result Found')

        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')
