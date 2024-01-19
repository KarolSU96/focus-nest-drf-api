from django.urls import path
from task_collections import views

urlpatterns= [
    path('task_collections/', views.TaskCollectionList.as_view()),
    path('task_collections/<int:pk>', views.TaskCollectionDetail.as_view()),
]