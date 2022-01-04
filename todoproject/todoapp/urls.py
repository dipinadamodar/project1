from django.contrib import admin
from django.urls import path

from . import views




urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('vlist/',views.TaskListView.as_view(),name='vlist'),
    path('dlist/<int:pk>/',views.TaskDetailView.as_view(),name='dlist'),
    path('listupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='listupdate'),
    path('listdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='listdelete'),



]