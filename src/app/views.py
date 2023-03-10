from django.shortcuts import get_object_or_404
from django.db.models import QuerySet
from rest_framework import status, viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.views import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import MultiPartRenderer, JSONRenderer
from drf_yasg.utils import swagger_auto_schema

from app.mixins import PermissionMixin
from app.renderers import ImageRenderer
from app.permissions import (
    IsReadOnly,
    IsOwnerCompanyOrCandidate, 
    IsCompany,
    IsCompanyAndOwnerVacancy,
    IsCandidate,
    IsCandidateAndOwnerExperience,
    IsCandidateAndOwnerReaction,
    IsCompanyAndOwnerVacancyOnReaction,
)
from app.models import Company, Vacancy, Candidate, Experience, Reaction
from app.serializers import (
    CompanySerializer, CompanyCreateSerializer, CompanyResponseSerializer,
    CandidateSerializer, CandidateCreateSerializer, CandidateResponseSerializer,
    VacancySerializer, VacancyUpdateSerializer, VacancyUploadImageSerializer,
    ExperienceSerializer, ExperienceUpdateSerializer,
    ReactionSerializer, ReactionUpdateSerializer, ReactionUpdateStatusSerializer,
)


class CompanyViewSet(PermissionMixin, viewsets.ViewSet):
    permission_classes_by_action = {
        'create': [AllowAny],
        'list': [IsAuthenticated],
        'list_vacancy': [IsAuthenticated],
        'list_reaction': [IsOwnerCompanyOrCandidate],
        'retrieve': [IsAuthenticated],
        'update': [IsOwnerCompanyOrCandidate],
        'destroy': [IsOwnerCompanyOrCandidate],
    }

    @swagger_auto_schema(
        request_body=CompanyCreateSerializer, 
        responses={201: CompanyResponseSerializer()}
    )
    def create(self, request: Request):
        serializer = CompanyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: CompanyResponseSerializer(many=True)})
    def list(self, request: Request):
        queryset = Company.objects.select_related('owner').all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)
        
    @swagger_auto_schema(responses={200: VacancySerializer(many=True)})
    @action(methods=['get'], url_path='vacancy', detail=True)
    def list_vacancy(self, request: Request, pk=None):
        company = get_object_or_404(Company, pk=pk)
        queryset = Vacancy.objects.filter(company=pk)
        serializer = VacancySerializer(instance=queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(responses={200: ReactionSerializer(many=True)})
    @action(detail=True, methods=['get'], url_path='reaction')
    def list_reaction(self, request: Request, pk=None):
        company: Company = get_object_or_404(Company.objects.all(), pk=pk)
        vacancies: QuerySet[int] = company.vacancies.values_list('id', flat=True)

        queryset = Reaction.objects.filter(vacancy__id__in=list(vacancies))
        serializer = ReactionSerializer(instance=queryset, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(responses={200: CompanyResponseSerializer()})
    def retrieve(self, request: Request, pk=None):
        queryset = Company.objects.select_related('owner').all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CompanySerializer, 
        responses={201: CompanyResponseSerializer()}
    )
    def update(self, request: Request, pk=None):
        instance = Company.objects.get(pk=pk)
        serializer = CompanySerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request: Request, pk=None):
        instance = Company.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CandidateViewSet(PermissionMixin, viewsets.ViewSet):
    permission_classes_by_action = {
        'create': [AllowAny],
        'list': [IsCompany],
        'list_experience': [IsOwnerCompanyOrCandidate|IsCompany],
        'list_reaction': [IsOwnerCompanyOrCandidate],
        'retrieve': [IsOwnerCompanyOrCandidate|IsCompany],
        'update': [IsOwnerCompanyOrCandidate],
        'destroy': [IsOwnerCompanyOrCandidate],
    }

    @swagger_auto_schema(
        request_body=CandidateCreateSerializer, 
        responses={201: CandidateResponseSerializer()}
    )
    def create(self, request: Request):
        serializer = CandidateCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: CandidateResponseSerializer(many=True)})
    def list(self, request: Request):
        queryset = Candidate.objects.select_related('user').all()
        serializer = CandidateSerializer(queryset, many=True)
        return Response(serializer.data)
        
    @swagger_auto_schema(responses={200: ExperienceSerializer(many=True)})
    @action(methods=['get'], url_path='experience', detail=True)
    def list_experience(self, request: Request, pk=None):
        candidate = get_object_or_404(Candidate, pk=pk)
        queryset = Experience.objects.filter(candidate=pk)
        serializer = ExperienceSerializer(instance=queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(responses={200: ReactionSerializer(many=True)})
    @action(methods=['get'], url_path='reaction', detail=True)
    def list_reaction(self, request: Request, pk=None):
        candidate = get_object_or_404(Candidate, pk=pk)
        queryset = Reaction.objects.filter(candidate=pk)
        serializer = ReactionSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: CandidateResponseSerializer()})
    def retrieve(self, request: Request, pk=None):
        queryset = Candidate.objects.select_related('user').all()
        candidate = get_object_or_404(queryset, pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CandidateSerializer, 
        responses={201: CandidateResponseSerializer()}
    )
    def update(self, request: Request, pk=None):
        instance = Candidate.objects.get(pk=pk)
        serializer = CandidateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request: Request, pk=None):
        instance = Candidate.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VacancyViewSet(PermissionMixin, viewsets.ViewSet):
    permission_classes_by_action = {
        'create': [IsCompany],
        'list': [AllowAny],
        'list_reaction': [IsCompanyAndOwnerVacancy],
        'retrieve': [AllowAny],
        'update': [IsCompanyAndOwnerVacancy],
        'upload_image': [IsReadOnly|IsCompanyAndOwnerVacancy],
        'destroy': [IsCompanyAndOwnerVacancy],
    }

    @swagger_auto_schema(request_body=VacancySerializer)
    def create(self, request: Request):
        serializer = VacancySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: VacancySerializer(many=True)})
    def list(self, request: Request):
        queryset = Vacancy.objects.all()
        serializer = VacancySerializer(queryset, many=True)
        return Response(serializer.data)
        
    @swagger_auto_schema(responses={200: ReactionSerializer(many=True)})
    @action(methods=['get'], url_path='reaction', detail=True)
    def list_reaction(self, request: Request, pk=None):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        queryset = Reaction.objects.filter(vacancy=pk)
        serializer = ReactionSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: VacancySerializer()})
    def retrieve(self, request: Request, pk=None):
        queryset = Vacancy.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = VacancySerializer(company)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=VacancyUpdateSerializer, responses={200: VacancySerializer()}
    )
    def update(self, request: Request, pk=None):
        instance = Vacancy.objects.get(pk=pk)
        serializer = VacancySerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema(method='get')
    @swagger_auto_schema(method='post', request_body=VacancyUploadImageSerializer)
    @action(
        methods=['post', 'get'], url_path='image', detail=True,
        parser_classes=[MultiPartParser],
        renderer_classes=[ImageRenderer, JSONRenderer]
    )
    def upload_image(self, request: Request, pk=None):
        instance = Vacancy.objects.get(pk=pk)
        if request.method == 'POST':
            serializer = VacancyUploadImageSerializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(instance.img.file, content_type='image/png')

    def destroy(self, request: Request, pk=None):
        instance = Vacancy.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExperienceViewSet(PermissionMixin, viewsets.ViewSet):
    permission_classes_by_action = {
        'create': [IsCandidate],
        'list': [IsCompany],
        'retrieve': [IsCompany|IsCandidateAndOwnerExperience],
        'update': [IsCandidateAndOwnerExperience],
        'destroy': [IsCandidateAndOwnerExperience],
    }

    @swagger_auto_schema(request_body=ExperienceSerializer)
    def create(self, request: Request):
        serializer = ExperienceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: ExperienceSerializer(many=True)})
    def list(self, request: Request):
        queryset = Experience.objects.all()
        serializer = ExperienceSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: ExperienceSerializer()})
    def retrieve(self, request: Request, pk=None):
        queryset = Experience.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = ExperienceSerializer(company)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ExperienceUpdateSerializer, 
        responses={200: ExperienceSerializer()}
    )
    def update(self, request: Request, pk=None):
        instance = Experience.objects.get(pk=pk)
        serializer = ExperienceSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request: Request, pk=None):
        instance = Experience.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReactionViewSet(PermissionMixin, viewsets.ViewSet):
    permission_classes_by_action = {
        'create': [IsCandidate],
        'list': [IsCompany],
        'retrieve': [IsCandidateAndOwnerReaction|IsCompanyAndOwnerVacancyOnReaction],
        'update': [IsCandidateAndOwnerReaction],
        # reaction status can update owner-candidate or
        # company that owns the vacancy for which reaction was written
        'update_status': [
            IsCandidateAndOwnerReaction|IsCompanyAndOwnerVacancyOnReaction
        ],
        'destroy': [IsCandidateAndOwnerReaction],
    }

    @swagger_auto_schema(request_body=ReactionSerializer)
    def create(self, request: Request):
        serializer = ReactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: ReactionSerializer(many=True)})
    def list(self, request: Request):
        queryset = Reaction.objects.all()
        serializer = ReactionSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: ReactionSerializer()})
    def retrieve(self, request: Request, pk=None):
        queryset = Reaction.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = ReactionSerializer(company)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ReactionUpdateSerializer, responses={200: ReactionSerializer()}
    )
    def update(self, request: Request, pk=None):
        instance = Reaction.objects.get(pk=pk)
        serializer = ReactionSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=ReactionUpdateStatusSerializer, 
        responses={200: ReactionSerializer()}
    )
    @action(methods=['put'], detail=True, url_path='status')
    def update_status(self, request: Request, pk=None):
        instance = Reaction.objects.get(pk=pk)
        serializer = ReactionSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request: Request, pk=None):
        instance = Reaction.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
