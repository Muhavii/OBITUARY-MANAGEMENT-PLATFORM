from django.urls import path
from . import views

urlpatterns = [
    path('', views.obituary_list, name='obituary_list'),
]
