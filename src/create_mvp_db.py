import httpx

from tests.utils import get_superuser_access_token
from tests.endpoints.data import (
    company_data, 
    vacancy_data, 
    candidate_data,
    experience_data,
    reaction_data,
)


BASE_URL = 'http://127.0.0.1:8000/api/v1/'


def get_authorization_headers(access_token: str):
    return {'AUTHORIZATION': f'Bearer {access_token}'}


def create_company_records():
    url = BASE_URL + 'company/'
    for data in company_data.create_company_valid:
        response = httpx.post(url=url, data=data)
        print('------------ Company:', response)


def create_candidate_records():
    url = BASE_URL + 'candidate/'
    for data in candidate_data.create_canditate_valid:
        response = httpx.post(url=url, data=data)
        print('------------ Candidate:', response)


def create_vacancy_records(access_token: str):
    url = BASE_URL + 'vacancy/'
    headers = get_authorization_headers(access_token)
    for data in vacancy_data.create_vacancy_valid:
        response = httpx.post(url=url, data=data, headers=headers)
        print('------------ Vacancy:', response)


def create_experience_records(access_token: str):
    url = BASE_URL + 'experience/'
    headers = get_authorization_headers(access_token)
    for data in experience_data.create_experience_valid:
        response = httpx.post(url=url, data=data, headers=headers)
        print('------------ Experience:', response)


def create_reaction_records(access_token: str):
    url = BASE_URL + 'reaction/'
    headers = get_authorization_headers(access_token)
    for data in reaction_data.create_reaction_valid:
        response = httpx.post(url=url, data=data, headers=headers)
        print('------------ Reaction:', response)


print('Start create MVP database...')

create_company_records()
create_candidate_records()

ACCESS_TOKEN: str = get_superuser_access_token()

create_vacancy_records(ACCESS_TOKEN)
create_experience_records(ACCESS_TOKEN)
create_reaction_records(ACCESS_TOKEN)

print('MVP database was creaded.')
