from django.urls import path
from task_collections import views

urlpatterns= [
    path('task_collections/', view.TaskCollectionList.as_view()),
]