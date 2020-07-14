from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def dynamic_lookup_view(request, product_id):
    obj = Product.objects.get(id=product_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def render_initial_data(request):
    initial_data = {
        'title': "New item"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
      'form': form
    }
    return render(request, "products/product_create.html", context)
