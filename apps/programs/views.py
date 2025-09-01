from django.shortcuts import render, redirect
from .models import Program

def program_list(request):
    programs = Program.objects.all()
    return render(request, "programs/program_list.html", {"programs": programs})

def program_create(request):
    if request.method == "POST":
        Program.objects.create(
            name=request.POST["name"],
            description=request.POST["description"],
            national_alignment=request.POST["national_alignment"],
            focus_areas=request.POST["focus_areas"],
            phases=request.POST["phases"],
        )
        return redirect("program_list")
    return render(request, "programs/program_form.html")
