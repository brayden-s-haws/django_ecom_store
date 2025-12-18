from django.shortcuts import render
from django.template.context_processors import request

from .models import Product

# Create your views here.
def index(request):
    product_objects = Product.objects.all()
    return render(request, 'shop/index.html', {'product_objects': product_objects})