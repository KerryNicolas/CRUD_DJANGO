
from django import forms
from .models import Employe

class EmployeForm (forms.ModelForm) :
    class Meta :
        model = Employe
        fields = ['nom', 'email', 'poste', 'salaire']
        widgets = {
            'nom' : forms.TextInput(attrs= {
                'class': 'input w-full',   
                'placeholder': ' Nom'
            }),
                'email' : forms.TextInput(attrs= {
                'class': 'input w-full',   
                'placeholder': ' Nom'
            }),
                'poste' : forms.TextInput(attrs= {
                'class': 'input w-full',   
                'placeholder': ' Nom'
            }),
                'salaire' : forms.TextInput(attrs= {
                'class': 'input w-full',   
                'placeholder': ' Nom'
            })
        }
