def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'participants/participant_confirm_delete.html', {'participant': participant})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant
from .forms import ParticipantForm

def participant_edit(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    form = ParticipantForm(request.POST or None, instance=participant)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('participant_list')
    return render(request, 'participants/participant_form.html', {'form': form, 'participant': participant})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant
from .forms import ParticipantForm
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

## assign_to_project view removed

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Participant
from apps.projects.models import Project

## assign_participant view removed

## remove_assignment view removed
