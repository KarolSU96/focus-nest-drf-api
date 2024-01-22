from rest_framework import serializers
from .models import Task
from profiles.models import Profile

class TaskSerializer(serializers.ModelSerializer):
    # Read-only field to display the owner's username
    owner = serializers.ReadOnlyField(source='owner.username')

    # Custom method to determine if the current user is the owner of the task
    is_owner = serializers.SerializerMethodField()

    # Read-only field to display the owner's profile ID
    profile_id = serializers.ReadOnlyField(source='owner.id')

    def get_is_owner(self, obj):
        # Custom method to check if the current user is the owner of the task
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = ['id','owner','profile_id','created_at','task_name','priority','is_done','due_date','notes','is_owner']