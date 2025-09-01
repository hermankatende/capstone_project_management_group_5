from django.shortcuts import render, redirect
from .models import Facility

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, "facilities/facility_list.html", {"facilities": facilities})

def facility_create(request):
    if request.method == "POST":
        Facility.objects.create(
            name=request.POST["name"],
            location=request.POST["location"],
            description=request.POST["description"],
            partner_organization=request.POST["partner_organization"],
            facility_type=request.POST["facility_type"],
            capabilities=request.POST["capabilities"],
        )
        return redirect("facility_list")
    return render(request, "facilities/facility_form.html")
