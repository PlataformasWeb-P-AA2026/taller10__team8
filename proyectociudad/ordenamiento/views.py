from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm


def _menu_links():
    return [
        {'url': 'ordenamiento:parroquias_list', 'label': 'Listar Parroquias'},
        {'url': 'ordenamiento:barrios_list', 'label': 'Listar Barrios'},
        {'url': 'ordenamiento:parroquia_create', 'label': 'Crear Parroquia'},
        {'url': 'ordenamiento:barrio_create', 'label': 'Crear Barrio'},
    ]


def parroquias_list(request):
    parroquias = Parroquia.objects.all()
    parroquia_data = []
    for parroquia in parroquias:
        barrios = Barrio.objects.filter(parroquia=parroquia).select_related('parroquia')
        barrio_data = []
        for barrio in barrios:
            presidente = getattr(barrio, 'presidentebarrio', None)
            barrio_data.append({
                'barrio': barrio,
                'presidente': presidente,
            })
        numero_parques = barrios.aggregate(total=Sum('numero_parques'))['total'] or 0
        parroquia_data.append({
            'parroquia': parroquia,
            'barrios': barrio_data,
            'numero_parques': numero_parques,
        })

    context = {
        'parroquia_data': parroquia_data,
        'menu_links': _menu_links(),
    }
    return render(request, 'ordenamiento/parroquias_list.html', context)


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
    return render(request, 'ordenamiento/parroquia_form.html', {
        'form': form,
        'menu_links': _menu_links(),
        'title': 'Crear Parroquia',
    })


def parroquia_edit(request, pk):
    parroquia = get_object_or_404(Parroquia, pk=pk)
    if request.method == 'POST':
        form = ParroquiaForm(request.POST, instance=parroquia)
        if form.is_valid():
            form.save()
            return redirect('ordenamiento:parroquias_list')
    else:
        form = ParroquiaForm(instance=parroquia)
    return render(request, 'ordenamiento/parroquia_form.html', {
        'form': form,
        'menu_links': _menu_links(),
        'title': 'Editar Parroquia',
    })


def barrio_create(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordenamiento:barrios_list')
    else:
        form = BarrioForm()
    return render(request, 'ordenamiento/barrio_form.html', {
        'form': form,
        'menu_links': _menu_links(),
        'title': 'Crear Barrio',
    })


def barrio_edit(request, pk):
    barrio = get_object_or_404(Barrio, pk=pk)
    if request.method == 'POST':
        form = BarrioForm(request.POST, instance=barrio)
        if form.is_valid():
            form.save()
            return redirect('ordenamiento:barrios_list')
    else:
        form = BarrioForm(instance=barrio)
    return render(request, 'ordenamiento/barrio_form.html', {
        'form': form,
        'menu_links': _menu_links(),
        'title': 'Editar Barrio',
    })
