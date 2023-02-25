'''After all these test we have company with id: 1, 2, 3, 4'''

import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from app.models import Company
from tests.endpoints.data import company_data


@pytest.mark.order(1)
@pytest.mark.parametrize(
    'request_data, response_data',
    [(a, b) for a, b in zip(
        company_data.create_company_valid, company_data.company_valid_reponse
    )]
)
def test_create_company(api_client: APIClient, request_data, response_data):
    url = reverse('company-list')
    response = api_client.post(url, data=request_data)

    assert response.status_code == 201
    assert response.json() == response_data


def test_create_company_invalid_password(api_client: APIClient):
    url = reverse('company-list')
    request_data = company_data.create_company_invalid_password
    response_data = company_data.create_company_invalid_password_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Company.objects.count() == 5


def test_create_company_invalid_required(api_client: APIClient):
    url = reverse('company-list')
    request_data = company_data.create_company_invalid_required
    response_data = company_data.create_company_invalid_required_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Company.objects.count() == 5


def test_create_company_invalid_unique(api_client: APIClient):
    url = reverse('company-list')
    request_data = company_data.create_company_invalid_unique
    response_data = company_data.create_company_invalid_unique_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Company.objects.count() == 5


def test_retrive_company(api_client: APIClient):
    url = reverse('company-detail', kwargs={'pk': 1})
    response_data = company_data.company_valid_reponse[0]
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_retrive_company_invalid_id(api_client: APIClient):
    url = reverse('company-detail', kwargs={'pk': 990})
    response_data = company_data.company_invalid_id_response
    response = api_client.get(url)

    assert response.status_code == 404
    assert response.json() == response_data


def test_list_company(api_client: APIClient):
    url = reverse('company-list')
    response_data = company_data.company_valid_reponse
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_update_company(api_client: APIClient):
    url = reverse('company-detail', kwargs={'pk': 5})
    request_data = company_data.update_company_valid
    response_data = company_data.update_company_valid_response
    response = api_client.put(url, data=request_data)

    assert response.status_code == 200
    assert response.json() == response_data


def test_delete_company(api_client: APIClient):
    url = reverse('company-detail', kwargs={'pk': 5})
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Company.objects.count() == 4
