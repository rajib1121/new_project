from django.urls import path
# from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hw/', views.hw, name='hw'),
    path('modal/', views.modal, name='modal'),
    path('form/', views.form, name='form'),
    path('country/', views.country, name='country'),
    path('hint/', views.hint, name='hint'),
    path('get_data/', views.get_data, name='get_data'),
    

]