from django.urls import path
from .import views



app_name = 'task'

urlpatterns = [
    path('',views.task_list,name='tasks_list'),
    path('create/',views.create_task,name='create_task'),
    path('delete/<int:task_id>/',views.delete_task,name='delete_task'),
    path('edit/<int:task_id>/',views.edit_task,name='edit_task'),
    path('complete/<int:task_id>/',views.task_done,name='done'),
    path('detail/<int:id>/',views.detail_task,name='detail'),
    path('approve/<int:id>/',views.approve,name='approve'),
    path('erase/',views.delete_all_approved,name='delete_all_approved'),
    path('remind/',views.march_reminder,name='remind'),
]
