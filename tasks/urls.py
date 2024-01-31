from django.urls import path
from tasks import views

urlpatterns = [
    # Endpoint for listing and creating tasks
    path("tasks/", views.TaskList.as_view()),
    # Endpoint for ndpoint for retrieving, updating, and deleting a specific task
    path("tasks/<int:pk>", views.TaskDetail.as_view()),
]
