from rest_framework import serializers
from .models import TaskCollection
from tasks.models import Task

class TaskCollectionSerializer(serializers.ModelSerializer):
    """
    Serializer for the TaskCollection model.

    - owner: The owner of the task collection (read-only).
    - is_owner: Indicates if the current user is the owner of the task collection.
    - tasks: Primary key related field representing the tasks associated with the task collection.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all(), required=False)

    def get_is_owner(self, obj):
        """
        Method to check if the current user is the owner of the task collection.

        Args:
        - obj: The TaskCollection instance.

        Returns:
        - True if the current user is the owner, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = TaskCollection
        fields = ['id','owner','title','due_date','created_at','description','tasks','is_owner']
