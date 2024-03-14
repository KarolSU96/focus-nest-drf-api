from rest_framework import generics, status, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskCollection
from drf_api.permissions import IsOwnerOrReadOnly
from .serializers import TaskCollectionSerializer
from django.db.models import Count


class TaskCollectionList(generics.ListCreateAPIView):
    queryset = TaskCollection.objects.annotate(num_tasks=Count("tasks"))
    serializer_class = TaskCollectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter collections based on the authenticated user
        return TaskCollection.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    search_fields = ["title", "description"]

    ordering_fields = [
        "due_date",
        "num_tasks",
    ]


class TaskCollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskCollection.objects.all()
    serializer_class = TaskCollectionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filter collections based on the authenticated user
        return TaskCollection.objects.filter(owner=self.request.user)
