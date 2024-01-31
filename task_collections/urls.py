from django.urls import path
from task_collections import views

urlpatterns = [
    # Endpoint for listing and creating task collections
    path("task_collections/", views.TaskCollectionList.as_view()),
    # Endpoint for retrieving, updating, deleting a specific task collection
    path("task_collections/<int:pk>", views.TaskCollectionDetail.as_view()),
]
