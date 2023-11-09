from django.shortcuts import render
from firstApp.forms import Formulario
from firstApp.models import Sala


def renderTemplate(request):
    return render(request,'firstApp/index.html')


def formulario(request):
    form = Formulario()
    if request.method == 'POST':
        form=Formulario(request.POST)
        if form.is_valid():
            form.save()
        return renderTemplate(request)
    data = {'form': form}
    return render(request,'firstApp/formulario.html',data)

def listadoSala(request):
    salas = Sala.objects.all()
    data = {'salas': salas}
    return render(request,'firstApp/listado.html', data)

def eliminarProyecto(request,id):
    sala=Sala.objects.get(id=id)
    sala.delete()
    return renderTemplate('/')

def actualizar(request,id):
    salas=Sala.objects.get(id=id)
    form=Formulario(instance=salas)
    if request.method=='POST':
        form=Formulario(request.POST,instance=salas)
        if form.is_valid():
            form.save()
        return renderTemplate(request)
    data={'form':form}
    return render(request,'firstApp/formulario.html', data)
# Create your views here.

