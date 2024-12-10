from django import forms
from .models import Evaluacion

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = [
            'documento', 'tipo_evalua', 'responsabilidad', 'sentido_de_pertenencia',
            'trabajo_en_equipo', 'liderazgo', 'humanizacion', 'seguridad', 'observaciones'
        ]
        widgets = {
            'tipo_evalua': forms.Select(),
            'responsabilidad': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'sentido_de_pertenencia': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'trabajo_en_equipo': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'liderazgo': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'humanizacion': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'seguridad': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'observaciones': forms.Textarea(attrs={'rows': 3})
        }