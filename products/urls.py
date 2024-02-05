from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('', views.catalog, name="index"),
    path('product/', views.product, name="product")
]
