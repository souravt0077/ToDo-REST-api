from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverView,name='apioverview'),
    path('task-list/',views.taskList,name='tasklist'),
    path('task-details/<str:pk>/',views.taskDetails,name='taskdetails'),
    path('task-create/',views.taskCreate,name='taskcreate'),
     path('task-update/<str:pk>/',views.taskUpdate,name='taskupdate'),
     path('task-delete/<str:pk>/',views.taskDelete,name='taskdelete'),
]
