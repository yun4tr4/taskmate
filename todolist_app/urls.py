from urllib import request
from django.urls import path
from todolist_app import views

urlpatterns = [
    path("", views.todolist, name= 'todolist'),
    path("abc/", views.abc, name='abc'),
    
    # path("about", views.about, name="about"),
    # path("contact", views.contact, name='contact'),
    
    path("delete/<task_id>", views.delete_task, name='delete_task'),
    path("edit/<task_id>", views.edit_task, name='edit_task'),
    path("complete/<task_id>", views.complete_task, name="complete_task"),
    path("pending/<task_id>", views.pending_task, name="pending_task"),
    
]
