from rest_framework.request import Request
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from app.utils import is_admin_or_superuser
from app.models import Vacancy, Experience, Reaction
from user.models import COMPANY_ALIAS, CANDIDATE_ALIAS


class IsReadOnly(BasePermission):
    '''
    Allow access only if request method in rest_framework.permissions.SAFE_METHODS
    '''
    def has_permission(self, request: Request, view) -> bool:
        return request.method in SAFE_METHODS


class IsOwnerCompanyOrCandidate(IsAuthenticated):
    '''
    Allow access only to authenticated users, owner of `Company` or `Candidate`
    and owner of requested `Company` or `Candidate`
    '''
    @is_admin_or_superuser
    def has_permission(self, request: Request, view) -> bool:
        if not super().has_permission(request, view):
            return False
        try:
            # take id company or candidate (example url /company/1/reaction/)
            object_id: int = int(request.parser_context.get('kwargs').get('pk'))
        except:
            # TODO: probably raise Exception() better
            return False
        # check if object_id is equal to id of the associated object of this user
        return object_id == request.user.get_related_object_id_by_user_type()
    

class IsCompany(IsAuthenticated):
    '''
    Allow access only to authenticated users and owner of the `Company`
    '''
    @is_admin_or_superuser
    def has_permission(self, request: Request, view) -> bool:
        if not super().has_permission(request, view):
            return False
        # check if user related object is Company
        return request.user.get_user_type() == COMPANY_ALIAS
    

class IsCompanyAndOwnerVacancy(IsCompany):
    '''
    Allow access only to authenticated users,
    owner of the `Company` and owner of the `Vacancy`
    '''
    @is_admin_or_superuser
    def has_permission(self, request: Request, view) -> bool:
        if not super().has_permission(request, view):
            return False
        try:
            # take id vacancy (example url /vacancy/1/)
            vacancy_id: int = request.parser_context.get('kwargs').get('pk')
            vacancy: Vacancy = Vacancy.objects.get(pk=vacancy_id)
        except:
            # TODO: probably raise Exception() better
            return False
        # check if company of vacancy is related object of user
        return vacancy.company == request.user.get_related_object_by_user_type()
    

class IsCandidate(IsAuthenticated):
    '''
    Allow access only to authenticated users and owner of the `Candidate`
    '''
    @is_admin_or_superuser
    def has_permission(self, request: Request, view) -> bool:
        if not super().has_permission(request, view):
            return False
        # check if user related object is Candidate
        return request.user.get_user_type() == CANDIDATE_ALIAS
    

class IsCandidateAndOwnerExperience(IsCandidate):
    '''
    Allow access only to authenticated users,
    owner of the `Candidate` and owner of the `Experience`
    '''
    @is_admin_or_superuser
    def has_permission(self, request: Request, view) -> bool:
        if not super().has_permission(request, view):
            return False
        try:
            # take id experience (example url /experience/1/)
            experience_id: int = request.parser_context.get('kwargs').get('pk')
            experience: Experience = Experience.objects.get(pk=experience_id)
        except:
            # TODO: probably raise Exception() better
            return False
        # check if candidate of experience is related object of user
        return experience.candidate == request.user.get_related_object_by_user_type()
    

class IsCandidateAndOwnerReaction(IsCandidate):
    '''
    Allow access only to authenticated users,
    owner of the `Candidate` and owner of the `Reaction`
    '''
    @is_admin_or_superuser
    def has_permission(self, request: Request, view) -> bool:
        if not super().has_permission(request, view):
            return False
        try:
            # take id reaction (example url /reaction/1/)
            reaction_id: int = request.parser_context.get('kwargs').get('pk')
            reaction: Reaction = Reaction.objects.get(pk=reaction_id)
        except:
            # TODO: probably raise Exception() better
            return False
        # check if candidate of reaction is related object of user
        return reaction.candidate == request.user.get_related_object_by_user_type()
    

class IsCompanyAndOwnerVacancyOnReaction(IsCompany):
    '''
    Allow access only to authenticated users,
    owner of the `Company` and the owner of `Vacancy` to which the `Reaction` is written
    '''
    @is_admin_or_superuser
    def has_permission(self, request: Request, view) -> bool:
        if not super().has_permission(request, view):
            return False
        try:
            # take id reaction (example url /reaction/1/)
            reaction_id: int = request.parser_context.get('kwargs').get('pk')
            reaction: Reaction = Reaction.objects.select_related('vacancy').\
                get(pk=reaction_id)
        except:
            # TODO: probably raise Exception() better
            return False
        # check if company of the vacancy is related object of user
        return reaction.vacancy.company == \
            request.user.get_related_object_by_user_type()
