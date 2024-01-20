from rest_framework import generics
from rest_framework.response import Response
from rest.rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import ContactForm
from .serializers import ContactFormSerializer

class ContactFormListView(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [IsAdminUser]

    def perforn_create(self, serializer):

        serializer.save(user=self.request.user)
