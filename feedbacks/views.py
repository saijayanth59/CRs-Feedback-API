from .models import Feedback, User
from .serializers import FeedbackSerializer
from rest_framework import generics


class FeedbackListCreate(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    
    def perform_create(self, serializer):
        try:
            user = User.objects.get(username=self.request.POST['id_number'])
        except:
            raise ValueError("Go away!")
        serializer.save(user=user)
