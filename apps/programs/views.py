from django.shortcuts import render, get_object_or_404, redirect
from .models import Program
from .forms import ProgramForm
from django.contrib import messages

def dashboard(request):
    # small dashboard showing counts and quick links
    data = {
        'program_count': Program.objects.count(),
        # later you can import other models counts for unified dashboard
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
