from rest_framework import serializers
from .models import User, Feedback


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'year', 'section')


class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    class Meta:
        model = Feedback
        fields = ('user', 'subject', 'teacher', 'taken', 'remarks', 'created')
