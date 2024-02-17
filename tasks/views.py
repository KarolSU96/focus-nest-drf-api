from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = {
        "is_done"
    }
    
    search_fields = [
        "task_name",
        "notes",
    ]
    ordering_fields = [
        "priority",
        "due_date",
        "is_done",
    ]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
