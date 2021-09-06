from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import GetAllTodoListView, CreateTaskView, DeleteAllTaskView, DeleteTaskView, UpdateTaskView, CheckAllTaskView, RemoveCheckAllTaskView

urlpatterns = [
    path('list-todo', GetAllTodoListView.as_view(), name='list-all-todo'),
    path('create-todo', CreateTaskView.as_view()),
    url(r'^update/(?P<id>\d+)$', UpdateTaskView.as_view(), name='update-task'),
    url(r'^delete/(?P<id>\d+)$', DeleteTaskView.as_view(), name='delete-task'),
    path('delete-all-todo', DeleteAllTaskView.as_view()),
    path('check-all-todo', CheckAllTaskView.as_view()),
    path('remove-check-all-todo', RemoveCheckAllTaskView.as_view())
]