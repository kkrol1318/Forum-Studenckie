# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cars', views.cars, name='cars'),
    path('contact', views.contact, name='contact'),
    path('kolo-1/', views.kolo1, name='kolo1'),
    path('kolo-2/', views.kolo2, name='kolo2'),
    path('kolo-3/', views.kolo3, name='kolo3'),
    path('kolo-4/', views.kolo4, name='kolo4'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('new_post', views.new_post, name='new_post'),
]
