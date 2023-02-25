from django.urls import path
from rest_framework import routers

from app.views import (
    CompanyViewSet, 
    CandidateViewSet,
    VacancyViewSet,
    ExperienceViewSet,
    ReactionViewSet
)


router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'candidate', CandidateViewSet, basename='candidate')
router.register(r'vacancy', VacancyViewSet, basename='vacancy')
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'reaction', ReactionViewSet, basename='reaction')


urlpatterns = [

] + router.urls
