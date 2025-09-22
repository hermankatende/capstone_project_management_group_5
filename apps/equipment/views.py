from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    """List all equipment."""
    equipment = Equipment.objects.select_related("facility").all()
    return render(request, "equipment/equipment_list.html", {"equipment": equipment})

def equipment_create(request):
    """Create a new equipment item."""
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipment added successfully.")
            return redirect("equipment_list")
    else:
        form = EquipmentForm()
    return render(request, "equipment/equipment_form.html", {"form": form})

def equipment_edit(request, pk):
    """Edit an existing equipment item."""
    eq = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=eq)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipment updated successfully.")
            return redirect("equipment_list")
    else:
        form = EquipmentForm(instance=eq)
    return render(request, "equipment/equipment_form.html", {"form": form, "equipment": eq})

def equipment_delete(request, pk):
    eq = get_object_or_404(Equipment, pk=pk)
    # Check if any active project in the same facility references this equipment
    from apps.projects.models import Project
    # Assuming a Project references Equipment via a field (not shown in your models),
    # if not, this logic can be adapted when such a relation exists.
    # For now, we check if any Project exists in the same facility (as a proxy for 'active usage')
    active_projects = Project.objects.filter(facility=eq.facility)
    # If you have a more direct relation, update this logic accordingly
    if active_projects.exists():
        messages.error(request, "Equipment referenced by active Project.")
        return redirect('equipment_list')
    if request.method == 'POST':
        eq.delete()
        messages.success(request, "Equipment deleted successfully.")
        return redirect('equipment_list')
    return render(request, 'equipment/equipment_confirm_delete.html', {'equipment': eq})
    """Delete an equipment item."""
    eq = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        eq.delete()
        messages.success(request, "Equipment deleted successfully.")
        return redirect("equipment_list")
    return render(request, "equipment/equipment_confirm_delete.html", {"equipment": eq})
