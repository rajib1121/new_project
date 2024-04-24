from django.urls import path
# from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hw/result/<str:keyword>', views.result, name='blog_result'),
    path('country/', views.country_page, name='blog_country'),
    path('modal/', views.modal_page, name='blog_modal'),
    path('form/', views.form_page, name='blog_form'),
    path('hw/', views.hw, name='blog_hw'),
    path('hint/', views.hint, name='blog_hint'),
    

]