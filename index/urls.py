from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('index', views.index, name='index'),
    path('shop_grid', views.shop_grid, name='shop_grid'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('checkout', views.checkout, name='checkout'),
    path('shop_details', views.shop_details, name='shop_details'),
    path('shoping_cart', views.shoping_cart, name='shoping_cart'),

]