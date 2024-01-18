from django.urls import path
from task_collections import views

urlpatterns= [
    path('task_collections/', views.TaskCollectionList.as_view()),
]