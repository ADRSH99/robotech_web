from django.urls import path
from . import views

urlpatterns = [
    path('<int:form_id>/', views.response_list, name='response_list'),
    path('edit/<int:response_id>/', views.edit_response, name='edit_response'),
]
