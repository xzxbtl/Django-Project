from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('registration/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout, name="logout")
]