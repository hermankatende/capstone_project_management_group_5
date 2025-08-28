from django.shortcuts import render, redirect
from .models import Program

def program_list(request):
    programs = Program.objects.all()
    return render(request, "programs/program_list.html", {"programs": programs})

def add_program(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        national_alignment = request.POST["national_alignment"]
        focus_areas = request.POST["focus_areas"]
        phases = request.POST["phases"]
        Program.objects.create(
            name=name,
            description=description,
            national_alignment=national_alignment,
            focus_areas=focus_areas,
            phases=phases
        )
        return redirect("program_list")
    return render(request, "programs/add_program.html")
