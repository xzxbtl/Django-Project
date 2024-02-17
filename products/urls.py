from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('search/', views.catalog, name="search"),
    path('<slug:category_slug>/', views.catalog, name="index"),
    path('product/<slug:product_slug>/', views.product, name="product")
]
