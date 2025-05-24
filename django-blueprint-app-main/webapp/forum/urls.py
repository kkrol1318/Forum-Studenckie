from django.urls import path
from . import views # from current folder import the neighbour file views for views methods usage

urlpatterns = [
    path('', views.index),
    path('frequent_questions', views.frequent_questions)
]
 

 # forum/urls.py
from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('join/<str:kolo>/', views.join_kolo,    name='join_kolo'),
    path('<str:kolo>/',        views.forum_view,  name='forum'),
]
