'''After all these test we have vacancy with id: 1, 2, 3, 4'''

import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from app.models import Vacancy
from tests.endpoints.data import vacancy_data

@pytest.mark.order(4)
@pytest.mark.parametrize(
    'request_data, response_data',
    [(a, b) for a, b in zip(
        vacancy_data.create_vacancy_valid, vacancy_data.vacancy_valid_reponse
    )]
)
def test_create_vacancy(api_client: APIClient, request_data, response_data):
    url = reverse('vacancy-list')
    response = api_client.post(url, data=request_data)

    assert response.status_code == 201
    assert response.json() == response_data


@pytest.mark.parametrize(
    'request_data, response_data',
    [(a, b) for a, b in zip(
        vacancy_data.create_vacancy_invalid_salary,
        vacancy_data.create_vacancy_invalid_salary_response
    )]
)
def test_create_vacancy_invalid_salary(
    api_client: APIClient, request_data, response_data
):
    url = reverse('vacancy-list')
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Vacancy.objects.count() == 5


def test_create_vacancy_invalid_required(api_client: APIClient):
    url = reverse('vacancy-list')
    request_data = vacancy_data.create_vacancy_invalid_required
    response_data = vacancy_data.create_vacancy_invalid_required_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Vacancy.objects.count() == 5


def test_create_vacancy_invalid_company_id(api_client: APIClient):
    url = reverse('vacancy-list')
    request_data = vacancy_data.create_vacancy_invalid_company_id
    response_data = vacancy_data.create_vacancy_invalid_company_id_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Vacancy.objects.count() == 5


def test_retrive_vacancy(api_client: APIClient):
    url = reverse('vacancy-detail', kwargs={'pk': 1})
    response_data = vacancy_data.vacancy_valid_reponse[0]
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_retrive_vacancy_invalid_id(api_client: APIClient):
    url = reverse('vacancy-detail', kwargs={'pk': 999})
    response_data = vacancy_data.vacancy_invalid_id_response
    response = api_client.get(url)

    assert response.status_code == 404
    assert response.json() == response_data


def test_list_vacancy(api_client: APIClient):
    url = reverse('vacancy-list')
    response_data = vacancy_data.vacancy_valid_reponse
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_list_vacancy_by_company(api_client: APIClient):
    # TODO: fix reverse name for this endpoint
    # url = reverse('retrieve-experience-detail', kwargs={'pk': 1})
    response_data = vacancy_data.vacancy_valid_reponse
    response = api_client.get('/api/v1/company/1/vacancy/')

    assert response.status_code == 200
    assert response.json() == response_data


def test_update_vacancy(api_client: APIClient):
    url = reverse('vacancy-detail', kwargs={'pk': 5})
    request_data = vacancy_data.update_vacancy_valid
    response_data = vacancy_data.update_vacancy_valid_response
    response = api_client.put(url, data=request_data)

    assert response.status_code == 200
    assert response.json() == response_data


def test_delete_vacancy(api_client: APIClient):
    url = reverse('vacancy-detail', kwargs={'pk': 5})
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Vacancy.objects.count() == 4
