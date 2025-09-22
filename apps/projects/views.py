from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

def project_list(request):
    """Show all projects."""
    projects = Project.objects.select_related('program', 'facility').order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_create(request):
    """Add a new project."""
    from apps.participants.models import Participant
    from apps.outcomes.models import Outcome
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        team_members = request.POST.getlist('team_members')
        status = request.POST.get('status', '').lower()
        if form.is_valid():
            project = form.save(commit=False)
            # Team tracking: must have at least one team member
            if not team_members:
                form.add_error(None, 'Project must have at least one team member assigned.')
            # Outcome validation: if status is 'completed', must have at least one outcome
            if status == 'completed':
                outcomes = Outcome.objects.filter(project=project)
                if not outcomes.exists():
                    form.add_error(None, 'Completed projects must have at least one documented outcome.')
            if not form.errors:
                project.save()
                # Save team members logic here if you have a relation
                messages.success(request, 'Project created successfully.')
                return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def project_edit(request, pk):
    """Edit an existing project."""
    from apps.participants.models import Participant
    from apps.outcomes.models import Outcome
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        team_members = request.POST.getlist('team_members')
        status = request.POST.get('status', '').lower()
        if form.is_valid():
            # Team tracking: must have at least one team member
            if not team_members:
                form.add_error(None, 'Project must have at least one team member assigned.')
            # Outcome validation: if status is 'completed', must have at least one outcome
            if status == 'completed':
                outcomes = Outcome.objects.filter(project=project)
                if not outcomes.exists():
                    form.add_error(None, 'Completed projects must have at least one documented outcome.')
            if not form.errors:
                form.save()
                # Save team members logic here if you have a relation
                messages.success(request, 'Project updated successfully.')
                return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'project': project})

def project_delete(request, pk):
    """Delete a project."""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully.')
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    assignments = project.projectparticipant_set.select_related("participant")
    return render(request, "projects/project_detail.html", {
        "project": project,
        "assignments": assignments,
    })
