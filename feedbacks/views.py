from .models import Feedback, User
from .serializers import FeedbackSerializer
from .filters import FeedbackFilter
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class FeedbackListCreate(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_class = FeedbackFilter
    filterset_fields = '__all__'
    
    def perform_create(self, serializer):
        try:
            user = User.objects.get(username=self.request.data['id_number'])
        except:
            raise ValueError("Go away!")
        serializer.save(user=user)
