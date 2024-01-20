from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import ContactForm
from .serializers import ContactFormSerializer

class ContactFormListView(generics.ListCreateAPIView):
    # Set the queryset to include all ContactForm instances
    queryset = ContactForm.objects.all()

    # Use the ContactFormSerializer for serialization
    serializer_class = ContactFormSerializer

    # Set the permission classes to only allow admin users to view the list
    permission_classes = [IsAdminUser]

    def perforn_create(self, serializer):

        serializer.save(user=self.request.user)

class ContactFormCreateView(generics.CreateAPIView):

    serializer_class = ContactFormSerializer