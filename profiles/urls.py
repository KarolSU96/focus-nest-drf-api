from django.urls import path
from profiles import views

urlpatterns = [
    # Endpoint for listing and creating profiles
    path("profiles/", views.ProfileList.as_view()),
    # Endpoint for retrieving, updating, and deleting a specific profile
    path("profiles/<int:pk>", views.ProfileDetail.as_view()),
]
