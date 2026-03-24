from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria


def main(request):
    return render(request, 'index.html')


def tienda(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'index.html', {
        'productos': productos,
        'categorias': categorias
    })


def productos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()

    return render(request, 'index.html', {
        'productos': productos,
        'categoria_actual': categoria,
        'categorias': categorias
    })