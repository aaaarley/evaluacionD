from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import EvaluacionForm
from .models import Evaluacion
import csv
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirige al home
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def home(request):
    return render(request, 'home.html', {'username': request.user.username})

@login_required
def home(request):
    # Manejar el formulario de evaluación
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            evaluacion = form.save(commit=False)
            evaluacion.usuario = request.user
            evaluacion.save()
            return redirect('/')
    else:
        form = EvaluacionForm()
    
    # Exportar a CSV
    if 'export_csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="evaluaciones.csv"'

        writer = csv.writer(response)
        writer.writerow(['Usuario', 'Fecha y Hora', 'Documento', 'Tipo de Evaluación',
                         'Responsabilidad', 'Sentido de Pertenencia', 'Trabajo en Equipo',
                         'Liderazgo', 'Humanización', 'Seguridad', 'Observaciones', 'Promedio'])
        
        evaluaciones = Evaluacion.objects.all()
        for eval in evaluaciones:
            writer.writerow([
                eval.usuario.username, eval.fecha_hora, eval.documento, eval.tipo_evalua,
                eval.responsabilidad, eval.sentido_de_pertenencia, eval.trabajo_en_equipo,
                eval.liderazgo, eval.humanizacion, eval.seguridad, eval.observaciones, eval.promedio
            ])
        return response

    # Obtener las evaluaciones del usuario actual
    evaluaciones_usuario = Evaluacion.objects.filter(usuario=request.user)

    return render(request, 'home.html', {
        'form': form,
        'evaluaciones_usuario': evaluaciones_usuario,
    })