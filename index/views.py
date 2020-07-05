from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Department, Product, ProductCatagory, Banner
from PIL import Image


# Create your views here.
def index(request):
    depatments = Department.objects.all()
    product_vegitables = Product.objects.all()
    product_categories = ProductCatagory.objects.all()

    if product_vegitables.count() > 3:
        latests = product_vegitables[len(product_vegitables) - 3:]
    else:
        latests = product_vegitables

    banner = Banner.objects.order_by('-id')[:3]

    # for i in range(len(latests)):
    #     img = latests[i].img
    #     image = str(latests[i].img)
    #     img_resize_110_latest(image)
    #     latests[i].img = img

    context = {
        'departments': depatments,
        'vegitables': product_vegitables,
        'types': product_categories,
        'latests': latests,
        'banner': banner,
    }
    return render(request, "index/index.html", context)


def contact(request):
    return render(request, "index/contact.html")


def shop_grid(request):
    return render(request, "index/shop_grid.html")


def blog(request):
    return render(request, "index/blog.html")


def blog_details(request):
    return render(request, "index/blog_details.html")


def checkout(request):
    return render(request, "index/checkout.html")


def shop_details(request):
    return render(request, "index/shop_details.html")


def shoping_cart(request):
    return render(request, "index/shoping_cart.html")


def img_resize_110_latest(image):
    img = Image.open("media/" + image)
    img.resize((110, 110))
    img.save("media/" + image)
