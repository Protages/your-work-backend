import httpx
from tests.endpoints.data import (
    company_data, 
    vacancy_data, 
    candidate_data,
    experience_data,
    reaction_data,
)


BASE_URL = 'http://127.0.0.1:8000/api/v1/'


def create_company_records():
    url = BASE_URL + 'company/'
    for data in company_data.create_company_valid:
        response = httpx.post(url=url, data=data)
        print('------------ Company:', response)


def create_vacancy_records():
    url = BASE_URL + 'vacancy/'
    for data in vacancy_data.create_vacancy_valid:
        response = httpx.post(url=url, data=data)
        print('------------ Vacancy:', response)


def create_candidate_records():
    url = BASE_URL + 'candidate/'
    for data in candidate_data.create_canditate_valid:
        response = httpx.post(url=url, data=data)
        print('------------ Candidate:', response)


def create_experience_records():
    url = BASE_URL + 'experience/'
    for data in experience_data.create_experience_valid:
        response = httpx.post(url=url, data=data)
        print('------------ Experience:', response)


def create_reaction_records():
    url = BASE_URL + 'reaction/'
    for data in reaction_data.create_reaction_valid:
        response = httpx.post(url=url, data=data)
        print('------------ Reaction:', response)


print('Start create MVP database...')

create_company_records()
create_vacancy_records()
create_candidate_records()
create_experience_records()
create_reaction_records()

print('MVP database was creaded.')
