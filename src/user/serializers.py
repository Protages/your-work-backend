from rest_framework import serializers

from .models import User
from app.custom_serializer import CustomSerializer
from app.serializers_mixins import CompanyMixin, CandidateMixin

from app.models import Candidate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
