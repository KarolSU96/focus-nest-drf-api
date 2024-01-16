from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.id')

    def get_is_owner(self, obj);
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = ['id','owner','created_at','task_name','priority','is_done','due_date','notes']