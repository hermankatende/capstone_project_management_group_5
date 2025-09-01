from django.shortcuts import render, get_object_or_404, redirect
from .models import Facility
from .forms import FacilityForm
from django.contrib import messages

def facility_list(request):
    facilities = Facility.objects.order_by('-created_at')
    return render(request,'facilities/facility_list.html',{'facilities':facilities})

def facility_create(request):
    if request.method=='POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Facility created.')
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request,'facilities/facility_form.html',{'form':form})

def facility_edit(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    form = FacilityForm(request.POST or None, instance=facility)
    if request.method=='POST' and form.is_valid():
        form.save()
        messages.success(request,'Facility updated.')
        return redirect('facility_list')
    return render(request,'facilities/facility_form.html',{'form':form,'facility':facility})

def facility_delete(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method=='POST':
        facility.delete()
        messages.success(request,'Facility deleted.')
        return redirect('facility_list')
    return render(request,'facilities/facility_confirm_delete.html',{'facility':facility})
