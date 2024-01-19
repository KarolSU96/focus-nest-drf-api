from rest_framework import generics
from rest_framework.response import Response
from .models import ContactForm
from .serializers import ContactFormSerializer

class ContactFormSubmissionListView(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
