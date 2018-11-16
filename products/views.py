from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.contrib.auth.decorators import login_required
from . models import Product

# Create your views here.

def home(request):
    time = datetime.datetime.today()
    return render(request, 'products/home.html',{'time':time})

@login_required
def create(request):
    time = datetime.datetime.today()
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon_pic'] and request.FILES['product_pic']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon_pic = request.FILES['icon_pic']
            product.product_pic = request.FILES['product_pic']
            product.title = datetime.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request,'products/create.html',{'error':"All fields are required!"})
    else:
        return render(request,'products/create.html',{'time':time})


def detail(request,product_id):
    pd = get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'pd':pd})
