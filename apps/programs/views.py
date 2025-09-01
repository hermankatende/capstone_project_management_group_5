from django.shortcuts import render, get_object_or_404, redirect
from .models import Program
from .forms import ProgramForm
from django.contrib import messages

def dashboard(request):
    from apps.projects.models import Project
    from apps.participants.models import Participant
    from apps.outcomes.models import Outcome
    from apps.facilities.models import Facility
    from apps.equipment.models import Equipment
    from apps.services.models import Service

    data = {
        'program_count': Program.objects.count(),
        'project_count': Project.objects.count(),
        'participant_count': Participant.objects.count(),
        'outcome_count': Outcome.objects.count(),
        'facility_count': Facility.objects.count(),
        'equipment_count': Equipment.objects.count(),
        'service_count': Service.objects.count(),
        'recent_programs': Program.objects.order_by('-created_at')[:5],
        'recent_projects': Project.objects.order_by('-created_at')[:5],
        'recent_outcomes': Outcome.objects.order_by('-created_at')[:5],
    }
    return render(request, 'programs/dashboard.html', data)

def program_list(request):
    programs = Program.objects.order_by('-created_at')
    return render(request, 'programs/program_list.html', {'programs': programs})

def program_create(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program created.')
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'programs/program_form.html', {'form': form})

def program_edit(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program updated.')
            return redirect('program_list')
    else:
        form = ProgramForm(instance=program)
    return render(request, 'programs/program_form.html', {'form': form, 'program': program})

def program_delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        messages.success(request, 'Program deleted.')
        return redirect('program_list')
    return render(request, 'programs/program_confirm_delete.html', {'program': program})
