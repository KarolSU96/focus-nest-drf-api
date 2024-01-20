from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # ReadOnlyField for the 'owner' field, showing the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')

    # SerializerMethodField for 'is_owner', a custom method to check if the request user is the owner
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        # Retrieve the request from the serializer context
        request = self.context['request']

        # Return True if the request user is the owner of the profile, False otherwise
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'name', 'image','total_tasks','total_collections','finished_tasks','current_goals','is_owner'
        ]