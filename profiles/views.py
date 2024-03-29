from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={"request": request}
        )
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    API view for retrieving, updating, and deleting a specific profile.

    - GET: Retrieves details of a specific profile.
    - PUT: Updates the details of a specific profile.
    """

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Helper method to get a specific profile by its primary key.

        Raises Http404 if the profile does not exist.

        Args:
        - pk: Primary key of the profile to retrieve.

        Returns:
        - The retrieved profile.
        """
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        GET method to retrieve details of a specific profile.

        Args:
        - request: Request object.
        - pk: Primary key of the profile to retrieve.

        Returns:
        - Response containing the serialized profile data.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
        PUT method to update details of a specific profile.

        Args:
        - request: Request object.
        - pk: Primary key of the profile to update.

        Returns:
        - Response containing the updated serialized profile data or errors.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
