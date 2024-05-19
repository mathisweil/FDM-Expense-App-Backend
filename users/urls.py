from django.urls import path
from . import views

urlpatterns = [
    path('get-users/<str:permission>/<int:employee_id>/', views.retrieve_employees,
         name='retrieve_employees'),
    path('get-user/<int:employee_id>/', views.retrieve_employee, name='retrieve_employee'),
    path('update-user/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('create-user/', views.create_employee, name='create_employee'),
    path('delete-user/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]
