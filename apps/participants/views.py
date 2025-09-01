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
