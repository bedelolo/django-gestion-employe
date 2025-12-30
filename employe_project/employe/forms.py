from django import forms
from .models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['Nom', 'Prenom', 'Email', 'Telephone', 'Poste', 'Salaire', 'Date_Embauche']
        widgets = {
            'Nom': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'Prenom': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'Email': forms.EmailInput(attrs={'class': 'input input-bordered w-full'}),
            'Telephone': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'Poste': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'Salaire': forms.NumberInput(attrs={'class': 'input input-bordered w-full'}),
            'Date_Embauche': forms.DateInput(attrs={'class': 'input input-bordered w-full', 'type': 'date'}),
        }
