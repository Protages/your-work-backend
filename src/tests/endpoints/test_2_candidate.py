'''After all these test we have candidate with id: 1, 2, 3, 4'''

import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from app.models import Candidate
from tests.endpoints.data import candidate_data

@pytest.mark.order(2)
@pytest.mark.parametrize(
    'request_data, response_data',
    [(a, b) for a, b in zip(
        candidate_data.create_canditate_valid, candidate_data.canditate_valid_reponse
    )]
)
def test_create_candidate(api_client: APIClient, request_data, response_data):
    url = reverse('candidate-list')
    response = api_client.post(url, data=request_data)

    assert response.status_code == 201
    assert response.json() == response_data


def test_create_candidate_invalid_password(api_client: APIClient):
    url = reverse('candidate-list')
    request_data = candidate_data.create_canditate_invalid_password
    response_data = candidate_data.create_canditate_invalid_password_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Candidate.objects.count() == 5


def test_create_candidate_invalid_required(api_client: APIClient):
    url = reverse('candidate-list')
    request_data = candidate_data.create_canditate_invalid_required
    response_data = candidate_data.create_canditate_invalid_required_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Candidate.objects.count() == 5


@pytest.mark.parametrize(
    'request_data', candidate_data.create_canditate_invalid_unique
)
def test_create_candidate_invalid_unique(api_client: APIClient, request_data):
    url = reverse('candidate-list')
    response_data = candidate_data.create_canditate_invalid_unique_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Candidate.objects.count() == 5


def test_retrive_candidate(api_client: APIClient):
    url = reverse('candidate-detail', kwargs={'pk': 1})
    response_data = candidate_data.canditate_valid_reponse[0]
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_retrive_candidate_invalid_id(api_client: APIClient):
    url = reverse('candidate-detail', kwargs={'pk': 999})
    response_data = candidate_data.candidate_invalid_id_response
    response = api_client.get(url)

    assert response.status_code == 404
    assert response.json() == response_data


def test_list_candidate(api_client: APIClient):
    url = reverse('candidate-list')
    response_data = candidate_data.canditate_valid_reponse
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_update_candidate(api_client: APIClient):
    url = reverse('candidate-detail', kwargs={'pk': 5})
    request_data = candidate_data.update_canditate_valid
    response_data = candidate_data.update_canditate_valid_response
    response = api_client.put(url, data=request_data)

    assert response.status_code == 200
    assert response.json() == response_data


def test_delete_candidate(api_client: APIClient):
    url = reverse('candidate-detail', kwargs={'pk': 5})
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Candidate.objects.count() == 4
