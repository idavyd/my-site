from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductFrom


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=10) ## get the list of all prods
    context = {
        'object': obj
    }
    return render(request,'products/product_detail.html', context)


def product_create_view1(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request,'products/product_create.html', context)

def product_create_view2(request):
    context = {
    }
    return render(request,'products/product_create.html', context)


def product_create_view(request):
    my_form = ProductForm(request.POST or None)
    context = {
        'form': my_form
    }
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()
    return render(request,'products/product_create.html', context)

