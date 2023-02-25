from django.conf import settings
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from app.models import Candidate


class CompanyMixin(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    employees = serializers.IntegerField()
    city = serializers.CharField(max_length=128)
    address = serializers.CharField(max_length=512, required=False)
    site = serializers.URLField(required=False)
    contact_email = serializers.EmailField(required=False)
    phone = PhoneNumberField(region=settings.PHONENUMBER_DEFAULT_REGION, required=False)
    tg = serializers.URLField(required=False)
    about = serializers.CharField()


class CandidateMixin(serializers.Serializer):
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    sex = serializers.ChoiceField(
        choices=Candidate.SEX, default=Candidate.NOT_CHOISEN, required=False
    )
    birthday = serializers.DateField(required=False)
    position = serializers.CharField(max_length=128)
    status = serializers.ChoiceField(
        choices=Candidate.CANDIDATE_STATUS,
        default=Candidate.SEARCH
    )
    salary = serializers.IntegerField(required=False)
    education = serializers.CharField(required=False)
    skills = serializers.CharField(required=False)
    about = serializers.CharField(required=False)
    contact_email = serializers.EmailField(required=False)
    phone = PhoneNumberField(
        region=settings.PHONENUMBER_DEFAULT_REGION, required=False
    )
    tg = serializers.URLField(required=False)
    city = serializers.CharField(max_length=128, required=False)
