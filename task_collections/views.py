from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskCollection
from .serializers import TaskCollectionSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class TaskCollectionList(APIView):
    """
    API view for listing and creating task collections.
    """

    serializer_class = TaskCollectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Retrieve a list of task collections.
        """
        task_collections = TaskCollection.objects.all()
        serializer = TaskCollectionSerializer(task_collections, many=True, context= {'request':request})
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new task collection.
        """
        serializer = TaskCollectionSerializer(
            data = request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskCollectionDetail(APIView):
    """
    API view for retrieving, updating, and deleting a specific task collection.
    """

    serializer_class = TaskCollectionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Retrieve a specific task collection by ID.
        """
        try:
            task_collection = TaskCollection.objects.get(pk=pk)
            self.check_object_permissions(self.request, task_collection)
            return task_collection
        except TaskCollection.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        """
        Retrieve details of a specific task collection.
        """
        task_collection = self.get_object(pk)
        serializer = TaskCollectionSerializer(
            task_collection, context= {'request':request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific task collection.
        """
        task_collection = self.get_object(pk)
        serializer = TaskCollectionSerializer(
            task_collection,data=request.data, context= {'request':request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific task collection.
        """
        task = self.get_object(pk)
        task.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


