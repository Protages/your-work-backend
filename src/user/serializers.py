from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer

from .models import User
from app.custom_serializer import CustomSerializer
from app.serializers_mixins import CompanyMixin, CandidateMixin

from app.models import Candidate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    account_type = serializers.CharField(read_only=True)
    related_obj_id = serializers.IntegerField(read_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        data['account_type'] = self.user.get_user_type()
        data['related_obj_id'] = self.user.get_related_object_id_by_user_type()
        return data
