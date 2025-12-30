from django.shortcuts import render, redirect, get_object_or_404
from .models import Employe
from .forms import EmployeForm

def listes_employes(request):
    employes = Employe.objects.all()
    return render(request, 'employe/list.html', {'employes': employes})

def ajouter_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listes_employes')
    else:
        form = EmployeForm()
    return render(request, 'employe/form.html', {'form': form, 'titre': 'Ajouter un employé'})

def modifier_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('listes_employes')
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'employe/form.html', {'form': form, 'titre': 'Modifier un employé'})

def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    if request.method == 'POST':
        employe.delete()
        return redirect('listes_employes')
    return render(request, 'employe/confirm_delete.html', {'employe': employe})

