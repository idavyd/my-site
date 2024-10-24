from django.shortcuts import render
from .models import Product, DroneProduct
from .forms import RawProductFrom
from django.db.models import Max


def product_detail_view(request, *args, **kwargs):
    products = DroneProduct.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/product_detail.html', context)


def dynamic_view(request, id,  *args, **kwargs):
    highest_id = DroneProduct.objects.aggregate(Max('id'))['id__max']
    if id <= highest_id:
        products = DroneProduct.objects.get(id=id)
        context = {
            'products': products
        }
        return render(request, 'products/dynamic_view.html', context)
    else:
        context = {
            'invalid_id': id
        }
        return render(request, 'products/wrong.html', context)


def product_create_view(request):
    form = RawProductFrom()
    if request.method == 'POST':
        form = RawProductFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            DroneProduct.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)




