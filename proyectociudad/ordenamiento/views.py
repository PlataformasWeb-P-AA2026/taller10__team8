from django.shortcuts import render, get_object_or_404, redirect
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm


def _menu_links():
    return [
        {'url': 'ordenamiento:parroquias_list', 'label': '[ Parroquias ]  '},
        {'url': 'ordenamiento:barrios_list', 'label': '[ Barrios ]  '},
        {'url': 'ordenamiento:parroquia_create', 'label': '[ + Parroquia ]'},
        {'url': 'ordenamiento:barrio_create', 'label': '[ + Barrio ]'},
    ]
def parroquias_list(request):
    parroquias = Parroquia.objects.all()
    parroquia_data = []
    for parroquia in parroquias:
        barrios =Barrio.objects.filter(parroquia=parroquia)
        barrio_data = []
        numero_parques = 0
        for barrio in barrios:
            try:
                presidente = barrio.presidentebarrio
            except:
                presidente = None
            # Sumar parques 
            numero_parques = numero_parques + barrio.numero_parques
            barrio_info = {
                'barrio': barrio,
                'presidente': presidente,
            }
            barrio_data.append(barrio_info)
        parroquia_info = {
            'parroquia': parroquia,
            'barrios': barrio_data,
            'numero_parques': numero_parques,}
        parroquia_data.append(parroquia_info)
    context = {
        'parroquia_data': parroquia_data,
        'menu_links': _menu_links()}
    return render(
        request,
        'ordenamiento/parroquias_list.html',
        context)

def barrios_list(request):
    barrios = Barrio.objects.select_related('parroquia').all()
    context = {
        'barrios': barrios,
        'menu_links': _menu_links(),
    }
    return render(request, 'ordenamiento/barrios_list.html', context)


def parroquia_create(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordenamiento:parroquias_list')
    else:
        form = ParroquiaForm()
        data={
            'form': form,
            'menu_links': _menu_links(),
            'title': 'Crear Parroquia',
        }
    return render(request, 'ordenamiento/parroquia_form.html', data)


def parroquia_edit(request, pk):
    parroquia = get_object_or_404(Parroquia, pk=pk)
    if request.method == 'POST':
        form = ParroquiaForm(request.POST, instance=parroquia)
        if form.is_valid():
            form.save()
            return redirect('ordenamiento:parroquias_list')
    else:
        form = ParroquiaForm(instance=parroquia)
        data ={
            'form': form,
            'menu_links': _menu_links(),
            'title': 'Editar Parroquia'
        }
    return render(request, 'ordenamiento/parroquia_form.html', data)


def barrio_create(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordenamiento:barrios_list')
    else:
        form = BarrioForm()
        data ={
            'form': form,
            'menu_links': _menu_links(),
            'title': 'Crear Barrio'
        }
    return render(request, 'ordenamiento/barrio_form.html', data)


def barrio_edit(request, pk):
    barrio = get_object_or_404(Barrio, pk=pk)
    if request.method == 'POST':
        form = BarrioForm(request.POST, instance=barrio)
        if form.is_valid():
            form.save()
            return redirect('ordenamiento:barrios_list')
    else:
        form = BarrioForm(instance=barrio)
        data={
            'form': form,
            'menu_links': _menu_links(),
            'title': 'Editar Barrio',
        }
    return render(request, 'ordenamiento/barrio_form.html', data)
