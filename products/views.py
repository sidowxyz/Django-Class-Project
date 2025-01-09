from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import products

# Create your views here.
def home(request):
    myproducts = products.objects.all()
    return render(request, 'home.html', {'products': myproducts})

def productDetail(request, id):
    product = get_object_or_404(products, product_id=id)  # Use 'id' instead of 'product_id'
    return render(request, 'productDetail.html', {'product': product})