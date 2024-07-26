from django.urls import path
from . import views

urlpatterns = [
    path("feedback/", views.FeedbackListCreate.as_view())
]