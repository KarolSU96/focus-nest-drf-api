from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
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

    def get_permissions(self):
        # Allow anyone (including logged-out users) to create contact forms
        if self.request.method == 'POST':
            return [AllowAny()]
        # Restrict view access to admin users
        return super().get_permissions()


class ContactFormCreateView(generics.CreateAPIView):
    serializer_class = ContactFormSerializer
