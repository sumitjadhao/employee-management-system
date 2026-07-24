from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_leave, name='apply_leave'),
    path('manage/', views.manage_leaves, name='manage_leaves'),
    path('update/<int:leave_id>/<str:new_status>/', views.update_leave_status, name='update_leave_status'),
]