from django.shortcuts import render, redirect, get_object_or_404
from .models import Outcome
from .forms import OutcomeForm

# List all outcomes
def outcome_list(request):
    outcomes = Outcome.objects.all()
    return render(request, 'outcome/outcome_list.html', {'outcomes': outcomes})

# View a single outcome's details
def outcome_detail(request, pk):
    outcome = get_object_or_404(Outcome, pk=pk)
    return render(request, 'outcome/outcome_detail.html', {'outcome': outcome})

# Create a new outcome
def outcome_create(request):
    if request.method == 'POST':
        form = OutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('outcome_list')
    else:
        form = OutcomeForm()
    return render(request, 'outcome/outcome_form.html', {'form': form})

# Edit an existing outcome
def outcome_edit(request, pk):
    outcome = get_object_or_404(Outcome, pk=pk)
    if request.method == 'POST':
        form = OutcomeForm(request.POST, instance=outcome)
        if form.is_valid():
            form.save()
            return redirect('outcome_list')
    else:
        form = OutcomeForm(instance=outcome)
    return render(request, 'outcome/outcome_form.html', {'form': form})

# Delete an outcome
def outcome_delete(request, pk):
    outcome = get_object_or_404(Outcome, pk=pk)
    if request.method == 'POST':
        outcome.delete()
        return redirect('outcome_list')
    return render(request, 'outcome/outcome_confirm_delete.html', {'outcome': outcome})
