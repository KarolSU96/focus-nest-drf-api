from rest_framework import serializers
from .models import TaskCollection
from tasks.models import Task

class TaskCollectionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all(), required=False)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = TaskCollection
        fields = ['id','owner','title','due_date','created_at','description','tasks','is_owner']
