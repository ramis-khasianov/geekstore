from django.urls import path
from .views import index, products

app_name = 'main_app'

urlpatterns = [
    path('', index, name='home'),
    path('products/', products, name='products')
]