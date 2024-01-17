from rest_framework import serializer
from .models import TaskCollection

class TaskCollectionSerializer(serializer.ModelSerializer):
    owner = serializer.ReadOnlyField(source='owner.username')
    is_owner = serializer.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = TaskCollection
        fields = ['id','owner','title','due_date','created_at','description','tasks','is_owner']