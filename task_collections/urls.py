from django.urls import path
from task_collection import views

urlpatterns= [
    path('task_collections/', view.TaskCollectionList.as_view()),
]