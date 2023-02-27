from django.conf import settings
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import ValidationError, UniqueTogetherValidator

from app.models import Company, Vacancy, Candidate, Experience, Reaction
from app.custom_serializer import CustomSerializer
from app.serializers_mixins import CompanyMixin, CandidateMixin
from app.utils import to_representation_with_user
from user.serializer_mixins import UserMixin
from user.models import User


class CompanyResponseSerializer(CustomSerializer, UserMixin, CompanyMixin):
    id = serializers.IntegerField(read_only=True)

    def to_representation(self, company: Company):
        '''Need to pass company with select_related(user) for optimization query'''
        user = company.owner
        return to_representation_with_user(self=self, instance=company, user=user)


class CompanyCreateSerializer(CustomSerializer, UserMixin, CompanyMixin):
    def create(self, validated_data: dict):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        if validated_data.get('contact_email', None) is None:
            validated_data.update({'contact_email': email})

        with transaction.atomic():
            company = Company.objects.create(**validated_data)
            user = User.objects.create(email=email, password=password, company=company)
        
        return company

    def to_representation(self, instance: Company):
        return CompanyResponseSerializer().to_representation(instance)

    def get_model(self):
        return Company


class CompanySerializer(CustomSerializer, CompanyMixin):
    def to_representation(self, instance: Company):
        return CompanyResponseSerializer().to_representation(instance)

    def get_model(self):
        return Company


class CandidateResponseSerializer(CustomSerializer, UserMixin, CandidateMixin):
    id = serializers.IntegerField(read_only=True)

    def to_representation(self, candidate: Candidate):
        '''Need to pass candidate with select_related(user) for optimization query'''
        user = candidate.user
        return to_representation_with_user(self=self, instance=candidate, user=user)
            

class CandidateCreateSerializer(CustomSerializer, UserMixin, CandidateMixin):
    def create(self, validated_data: dict):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        if validated_data.get('contact_email', None) is None:
            validated_data.update({'contact_email': email})

        with transaction.atomic():
            candidate = Candidate.objects.create(**validated_data)
            user = User.objects.create(
                email=email, password=password, candidate=candidate
            )
        
        return candidate

    def to_representation(self, instance: Candidate):
        return CandidateResponseSerializer().to_representation(instance)

    def get_model(self):
        return Candidate


class CandidateSerializer(CustomSerializer, CandidateMixin):
    def to_representation(self, instance: Candidate):
        return CandidateResponseSerializer().to_representation(instance)

    def get_model(self):
        return Candidate


class VacancyUploadImageSerializer(CustomSerializer):
    img = serializers.ImageField()

    def create(self, validated_data: dict):
        raise Exception(
            'VacancyUploadImageSerializer dosnt create instance, only update'
        )

    def update(self, instance: Vacancy, validated_data: dict) -> Vacancy:
        instance.img = validated_data.get('img')
        instance.save()
        return instance

    def get_model(self):
        return Vacancy


class VacancyUpdateSerializer(CustomSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=128)
    salary = serializers.IntegerField()
    required_experience = serializers.IntegerField(required=False)
    skills = serializers.CharField()
    description = serializers.CharField()

    def validate_salary(self, value: int) -> int:
        if value < settings.MIN_SALARY:
            raise ValidationError(
                detail=f'Too small value, min value {settings.MIN_SALARY}'
            )
        elif value > settings.MAX_SALARY:
            raise ValidationError(
                detail=f'Too big value, max value {settings.MAX_SALARY}'
            )
        return value

    def get_model(self):
        return Vacancy


class VacancySerializer(VacancyUpdateSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())


class ExperienceUpdateSerializer(CustomSerializer):
    id = serializers.IntegerField(read_only=True)
    company = serializers.CharField(max_length=128)
    position = serializers.CharField(max_length=128)
    start = serializers.DateField()
    end = serializers.DateField(required=False)
    description = serializers.CharField(required=False)
    
    def validate(self, attrs):
        start = attrs.get('start')
        end = attrs.get('end', None)
        if end is not None and end <= start:
            raise ValidationError(
                detail='End date must be more then start date, or None'
            )
        return super().validate(attrs)

    def get_model(self):
        return Experience


class ExperienceSerializer(ExperienceUpdateSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())


class ReactionUpdateSerializer(CustomSerializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(
        choices=Reaction.REACTION_STATUS, default=Reaction.NOT_VIEWED
    )
    comment = serializers.CharField(required=False)
    cv = serializers.FileField(required=False)

    def get_model(self):
        return Reaction


class ReactionSerializer(ReactionUpdateSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
    vacancy = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all())

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Reaction.objects.all(),
                fields=['candidate', 'vacancy']
            )
        ]
