from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskCollection
from .serializers import TaskCollectionSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class TaskCollectionList(generics.ListCreateAPIView):
    queryset = TaskCollection.objects.all()
    serializer_class = TaskCollectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class TaskCollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskCollection.objects.all()
    serializer_class = TaskCollectionSerializer
    permission_classes = [IsOwnerOrReadOnly]