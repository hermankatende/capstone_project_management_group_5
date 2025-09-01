from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm
from facilities.models import Facility
from django.contrib import messages

def service_list(request):
    services = Service.objects.select_related('facility').order_by('-created_at')
    return render(request,'services/service_list.html',{'services':services})

def service_create(request):
    if request.method=='POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Service created.')
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request,'services/service_form.html',{'form':form})

def service_edit(request, pk):
    s = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=s)
    if request.method=='POST' and form.is_valid():
        form.save()
        messages.success(request,'Service updated.')
        return redirect('service_list')
    return render(request,'services/service_form.html',{'form':form,'service':s})

def service_delete(request, pk):
    s = get_object_or_404(Service, pk=pk)
    if request.method=='POST':
        s.delete()
        messages.success(request,'Service deleted.')
        return redirect('service_list')
    return render(request,'services/service_confirm_delete.html',{'service':s})
