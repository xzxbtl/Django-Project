from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about")
]
