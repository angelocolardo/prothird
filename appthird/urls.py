from django.urls import include, path
from appthird import views

urlpatterns = [
    path('', views.index, name = 'index'),
]
