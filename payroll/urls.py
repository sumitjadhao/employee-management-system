from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_payroll, name='generate_payroll'),
    path('list/', views.payroll_list, name='payroll_list'),
    path('my-salary/', views.my_salary, name='my_salary'),
]