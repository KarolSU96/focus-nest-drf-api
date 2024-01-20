from django.urls import path
from contact_forms import views

urlpatterns= [
    path('contact_forms/',views.ContactFormListView.as_view()),
]
