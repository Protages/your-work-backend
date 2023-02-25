'''Data for reaction endpoint tests'''

from app.models import Reaction


create_reaction_valid = [
    {  # Max data
        "candidate": 1,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": "some_comment1"
    },
    {
        "candidate": 1,
        "vacancy": 2,
        "status": Reaction.VIEWED,
        "comment": "some_comment2"
    },
    {  # Min data
        "candidate": 1,
        "vacancy": 3
    },
    {
        "candidate": 1,
        "vacancy": 4
    },
    {
        "candidate": 2,
        "vacancy": 1
    },
    {
        "candidate": 3,
        "vacancy": 1
    },
    {
        "candidate": 4,
        "vacancy": 1
    },
    {
        "candidate": 2,
        "vacancy": 2
    }
]

reaction_objects_count = len(create_reaction_valid)

reaction_valid_reponse = [
    {
        'id': 1,
        "candidate": 1,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": "some_comment1",
        'cv': None
    },
    {
        'id': 2,
        "candidate": 1,
        "vacancy": 2,
        "status": Reaction.VIEWED,
        "comment": "some_comment2",
        'cv': None
    },
    {
        'id': 3,
        "candidate": 1,
        "vacancy": 3,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 4,
        "candidate": 1,
        "vacancy": 4,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 5,
        "candidate": 2,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 6,
        "candidate": 3,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 7,
        "candidate": 4,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 8,
        "candidate": 2,
        "vacancy": 2,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    }
]

reaction_valid_reponse_candidate_id1 = [
    {
        'id': 1,
        "candidate": 1,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": "some_comment1",
        'cv': None
    },
    {
        'id': 2,
        "candidate": 1,
        "vacancy": 2,
        "status": Reaction.VIEWED,
        "comment": "some_comment2",
        'cv': None
    },
    {
        'id': 3,
        "candidate": 1,
        "vacancy": 3,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 4,
        "candidate": 1,
        "vacancy": 4,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    }
]

reaction_valid_reponse_vacancy_id1 = [
    {
        'id': 1,
        "candidate": 1,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": "some_comment1",
        'cv': None
    },
    {
        'id': 5,
        "candidate": 2,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 6,
        "candidate": 3,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    },
    {
        'id': 7,
        "candidate": 4,
        "vacancy": 1,
        "status": Reaction.NOT_VIEWED,
        "comment": None,
        'cv': None
    }
]

reaction_valid_reponse_company_id1 = reaction_valid_reponse

create_reaction_invalid_unique_together = {
    "candidate": 1,  # alredy exist candidate-1 with vacancy-1
    "vacancy": 1
}

create_reaction_invalid_unique_together_response = {
    'non_field_errors': ['The fields candidate, vacancy must make a unique set.']
}

create_reaction_invalid_required = {
    "status": Reaction.NOT_VIEWED,
}

create_reaction_invalid_required_reponse = {
    'candidate': ['This field is required.'], 
    'vacancy': ['This field is required.']
}

create_reaction_invalid_candidate_id = {
    "candidate": 999,
    "vacancy": 1
}

create_reaction_invalid_candidate_id_reponse = {
    'candidate': ['Invalid pk "999" - object does not exist.']
}

create_reaction_invalid_vacancy_id = {
    "candidate": 1,
    "vacancy": 999
}

create_reaction_invalid_vacancy_id_reponse = {
    'vacancy': ['Invalid pk "999" - object does not exist.']
}

reaction_invalid_id_response = {'detail': 'Not found.'}

update_reaction_valid = {
    "status": Reaction.REJECT,
    "comment": "new_comment999"
}

update_reaction_valid_response= {
    'id': 8,
    "candidate": 2,
    "vacancy": 2,
    "status": Reaction.REJECT,
    "comment": "new_comment999",
    'cv': None
}
