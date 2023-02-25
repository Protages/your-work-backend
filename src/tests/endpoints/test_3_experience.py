'''After all these test we have experience with id: 1, 2, 3, 4'''

import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from app.models import Experience
from tests.endpoints.data import experience_data, candidate_data

@pytest.mark.order(3)
@pytest.mark.parametrize(
    'request_data, response_data',
    [(a, b) for a, b in zip(
        experience_data.create_experience_valid, 
        experience_data.experience_valid_reponse
    )]
)
def test_create_experience(api_client: APIClient, request_data, response_data):
    url = reverse('experience-list')
    response = api_client.post(url, data=request_data)

    assert response.status_code == 201
    assert response.json() == response_data


def test_create_experience_invalid_start_end(api_client: APIClient):
    url = reverse('experience-list')
    request_data = experience_data.create_experience_invalid_start_end
    response_data = experience_data.create_experience_invalid_start_end_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Experience.objects.count() == 5


def test_create_experience_invalid_candidate_id(api_client: APIClient):
    url = reverse('experience-list')
    request_data = experience_data.create_experience_invalid_candidate_id
    response_data = experience_data.create_experience_invalid_candidate_id_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Experience.objects.count() == 5


def test_create_experience_invalid_requered(api_client: APIClient):
    url = reverse('experience-list')
    request_data = experience_data.create_experience_invalid_required
    response_data = experience_data.create_experience_invalid_required_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Experience.objects.count() == 5


def test_retrive_experience(api_client: APIClient):
    url = reverse('experience-detail', kwargs={'pk': 1})
    response_data = experience_data.experience_valid_reponse[0]
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_retrive_experience_invalid_id(api_client: APIClient):
    url = reverse('experience-detail', kwargs={'pk': 999})
    response_data = experience_data.experience_invalid_id_response
    response = api_client.get(url)

    assert response.status_code == 404
    assert response.json() == response_data


def test_list_experience(api_client: APIClient):
    url = reverse('experience-list')
    response_data = experience_data.experience_valid_reponse
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_list_experience_by_candidate(api_client: APIClient):
    # TODO: fix reverse name for this endpoint
    # url = reverse('retrieve-experience-detail', kwargs={'pk': 1})
    response_data = experience_data.experience_valid_reponse
    response = api_client.get('/api/v1/candidate/1/experience/')

    assert response.status_code == 200
    assert response.json() == response_data


def test_update_experience(api_client: APIClient):
    url = reverse('experience-detail', kwargs={'pk': 5})
    request_data = experience_data.update_experience_valid
    response_data = experience_data.update_experience_valid_response
    response = api_client.put(url, data=request_data)

    assert response.status_code == 200
    assert response.json() == response_data


def test_delete_experience(api_client: APIClient):
    url = reverse('experience-detail', kwargs={'pk': 5})
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Experience.objects.count() == 4
