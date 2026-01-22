from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_list, name='form_list'),
    path('create/', views.create_form, name='create_form'),
    path('<uuid:public_id>/', views.public_form, name='public_form'),
]
