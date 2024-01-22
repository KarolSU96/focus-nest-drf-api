from rest_framework import generics, status, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskCollection
from .serializers import TaskCollectionSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class TaskCollectionList(generics.ListCreateAPIView):
    queryset = TaskCollection.objects.all()
    serializer_class = TaskCollectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    search_fields = [
        'title',
        'description'
    ]

    ordering_fields = [
        'due_date',
        'tasks',
    ]

class TaskCollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskCollection.objects.all()
    serializer_class = TaskCollectionSerializer
    permission_classes = [IsOwnerOrReadOnly]
