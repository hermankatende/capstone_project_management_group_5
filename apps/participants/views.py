from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant, ProjectParticipant
from .forms import ParticipantForm, ProjectParticipantForm
from django.contrib import messages

def participant_list(request):
    people = Participant.objects.order_by('-created_at')
    return render(request,'participants/participant_list.html',{'people':people})

def participant_create(request):
    if request.method=='POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Participant added.')
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request,'participants/participant_form.html',{'form':form})

def assign_to_project(request):
    if request.method=='POST':
        form = ProjectParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Assigned participant to project.')
            return redirect('participant_list')
    else:
        form = ProjectParticipantForm()
    return render(request,'participants/assign_form.html',{'form':form})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Participant, ProjectParticipant
from apps.projects.models import Project

def assign_participant(request, project_id):
    """Assign a participant to a project with a role."""
    project = get_object_or_404(Project, pk=project_id)
    participants = Participant.objects.all()

    if request.method == "POST":
        participant_id = request.POST["participant"]
        role_on_project = request.POST["role_on_project"]
        skill_role = request.POST["skill_role"]

        ProjectParticipant.objects.create(
            project=project,
            participant_id=participant_id,
            role_on_project=role_on_project,
            skill_role=skill_role
        )
        messages.success(request, "Participant assigned successfully.")
        return redirect("project_detail", pk=project_id)

    return render(request, "participants/assign_participant.html", {
        "project": project,
        "participants": participants
    })

def remove_assignment(request, assignment_id):
    """Remove a participant from a project."""
    assignment = get_object_or_404(ProjectParticipant, pk=assignment_id)
    project_id = assignment.project.pk
    assignment.delete()
    messages.success(request, "Participant removed from project.")
    return redirect("project_detail", pk=project_id)
