'''After all these test we have responses with id: 1, 2, 3, 4, 5, 6, 7'''

import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from app.models import Reaction
from tests.endpoints.data import reaction_data

@pytest.mark.order(5)
@pytest.mark.parametrize(
    'request_data, response_data',
    [(a, b) for a, b in zip(
        reaction_data.create_reaction_valid, 
        reaction_data.reaction_valid_reponse
    )]
)
def test_create_reaction(api_client: APIClient, request_data, response_data):
    url = reverse('reaction-list')
    response = api_client.post(url, data=request_data)

    assert response.status_code == 201
    assert response.json() == response_data


def test_create_reaction_invalid_unique_together(api_client: APIClient):
    url = reverse('reaction-list')
    request_data = reaction_data.create_reaction_invalid_unique_together
    response_data = reaction_data.create_reaction_invalid_unique_together_response
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Reaction.objects.count() == reaction_data.reaction_objects_count


def test_create_reaction_invalid_required(api_client: APIClient):
    url = reverse('reaction-list')
    request_data = reaction_data.create_reaction_invalid_required
    response_data = reaction_data.create_reaction_invalid_required_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Reaction.objects.count() == reaction_data.reaction_objects_count


def test_create_reaction_invalid_candidate_id(api_client: APIClient):
    url = reverse('reaction-list')
    request_data = reaction_data.create_reaction_invalid_candidate_id
    response_data = reaction_data.create_reaction_invalid_candidate_id_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Reaction.objects.count() == reaction_data.reaction_objects_count


def test_create_reaction_invalid_vacancy_id(api_client: APIClient):
    url = reverse('reaction-list')
    request_data = reaction_data.create_reaction_invalid_vacancy_id
    response_data = reaction_data.create_reaction_invalid_vacancy_id_reponse
    response = api_client.post(url, data=request_data)

    assert response.status_code == 400
    assert response.json() == response_data
    assert Reaction.objects.count() == reaction_data.reaction_objects_count


def test_retrive_reaction(api_client: APIClient):
    url = reverse('reaction-detail', kwargs={'pk': 1})
    response_data = reaction_data.reaction_valid_reponse[0]
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_retrive_reaction_invalid_id(api_client: APIClient):
    url = reverse('reaction-detail', kwargs={'pk': 999})
    response_data = reaction_data.reaction_invalid_id_response
    response = api_client.get(url)

    assert response.status_code == 404
    assert response.json() == response_data


def test_list_reaction(api_client: APIClient):
    url = reverse('reaction-list')
    response_data = reaction_data.reaction_valid_reponse
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == response_data


def test_list_reaction_by_candidate(api_client: APIClient):
    # TODO: fix reverse name for this endpoint
    # url = reverse('retrieve-experience-detail', kwargs={'pk': 1})
    response_data = reaction_data.reaction_valid_reponse_candidate_id1
    response = api_client.get('/api/v1/candidate/1/reaction/')

    assert response.status_code == 200
    assert response.json() == response_data


def test_list_reaction_by_vacancy(api_client: APIClient):
    # TODO: fix reverse name for this endpoint
    # url = reverse('retrieve-experience-detail', kwargs={'pk': 1})
    response_data = reaction_data.reaction_valid_reponse_vacancy_id1
    response = api_client.get('/api/v1/vacancy/1/reaction/')

    assert response.status_code == 200
    assert response.json() == response_data


def test_list_reaction_by_company(api_client: APIClient):
    # TODO: fix reverse name for this endpoint
    # url = reverse('retrieve-experience-detail', kwargs={'pk': 1})
    response_data = reaction_data.reaction_valid_reponse_company_id1
    response = api_client.get('/api/v1/company/1/reaction/')

    assert response.status_code == 200
    assert len(response.json()) == len(response_data)
    for reaction in response_data:
        assert reaction in response.json()


def test_update_reaction(api_client: APIClient):
    url = reverse('reaction-detail', kwargs={
        'pk': reaction_data.reaction_objects_count
    })
    request_data = reaction_data.update_reaction_valid
    response_data = reaction_data.update_reaction_valid_response
    response = api_client.put(url, data=request_data)

    assert response.status_code == 200
    assert response.json() == response_data


def test_delete_reaction(api_client: APIClient):
    url = reverse('reaction-detail', kwargs={
        'pk': reaction_data.reaction_objects_count
    })
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Reaction.objects.count() == reaction_data.reaction_objects_count - 1
