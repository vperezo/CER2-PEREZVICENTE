from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import LugarPatrimonial, Categoria
from .forms import LugarForm

def home(request):
    destacados = LugarPatrimonial.objects.filter(destacado=True)[:3]
    return render(request, 'core/home.html', {'destacados': destacados})

def catalogo(request):
    categoria_id = request.GET.get('categoria', '')
    lugares = LugarPatrimonial.objects.all()
    if categoria_id.isdigit():
        lugares = lugares.filter(categoria__id=categoria_id)
    data = {
        'lugares': lugares,
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'core/catalogo.html', data)

def detalle(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    return render(request, 'core/detalle.html', {'lugar': lugar})

@login_required
def gestion(request):
    lugares = LugarPatrimonial.objects.all().order_by('nombre')
    return render(request, 'core/gestion.html', {'lugares': lugares})

@login_required
@permission_required('core.add_lugarpatrimonial', raise_exception=True)
def agregar(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = LugarForm()
    return render(request, 'core/lugar_form.html', {'form': form, 'titulo': 'Agregar lugar'})

@login_required
@permission_required('core.change_lugarpatrimonial', raise_exception=True)
def editar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    if request.method == 'POST':
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = LugarForm(instance=lugar)
    return render(request, 'core/lugar_form.html', {'form': form, 'titulo': 'Editar lugar'})

