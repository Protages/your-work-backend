'''Data for experience endpoint tests'''


create_experience_valid = [
    {  # Max data
        "company": "Some Company 1",
        "position": "Backend Developer",
        "start": "2015-02-25",
        "end": "2016-02-25",
        "description": "some_description",
        "candidate": 1
    },
    {  # Min data
        "company": "Some Company 2",
        "position": "Fullstack Developer",
        "start": "2016-02-26",
        "end": "2017-02-25",
        "candidate": 1
    },
    {
        "company": "Some Company 3",
        "position": "Backend Developer",
        "start": "2017-02-26",
        "end": "2018-02-25",
        "candidate": 1
    },
    {
        "company": "Some Company 4",
        "position": "Backend Developer",
        "start": "2018-02-26",
        "end": "2019-02-25",
        "candidate": 1
    },
    {  # Data without end
        "company": "Some Company 5",
        "position": "Backend Developer",
        "start": "2018-02-26",
        "candidate": 1
    }
]

experience_valid_reponse = [
    {
        'id': 1,
        "company": "Some Company 1",
        "position": "Backend Developer",
        "start": "2015-02-25",
        "end": "2016-02-25",
        "description": "some_description",
        "candidate": 1
    },
    {
        'id': 2,
        "company": "Some Company 2",
        "position": "Fullstack Developer",
        "start": "2016-02-26",
        "end": "2017-02-25",
        "description": None,
        "candidate": 1
    },
    {
        'id': 3,
        "company": "Some Company 3",
        "position": "Backend Developer",
        "start": "2017-02-26",
        "end": "2018-02-25",
        "description": None,
        "candidate": 1
    },
    {
        'id': 4,
        "company": "Some Company 4",
        "position": "Backend Developer",
        "start": "2018-02-26",
        "end": "2019-02-25",
        "description": None,
        "candidate": 1
    },
    {
        'id': 5,
        "company": "Some Company 5",
        "position": "Backend Developer",
        "start": "2018-02-26",
        "end": None,
        "description": None,
        "candidate": 1
    }
]

create_experience_invalid_start_end= {
    "company": "Some Company 999",
    "position": "Backend Developer",
    "start": "2018-02-26",
    "end": "2000-02-25",
    "candidate": 1
}

create_experience_invalid_start_end_reponse = {
    'non_field_errors': ['End date must be more then start date, or None']
}

create_experience_invalid_candidate_id = {
    "company": "Some Company 999",
    "position": "Backend Developer",
    "start": "2018-02-26",
    "end": "2019-02-25",
    "candidate": 999
}

create_experience_invalid_candidate_id_reponse = {
    'candidate': ['Invalid pk "999" - object does not exist.']
}

create_experience_invalid_required = {
    "company": "Some Company 999"
}

create_experience_invalid_required_reponse = {
    'position': ['This field is required.'], 
    'start': ['This field is required.'], 
    'candidate': ['This field is required.']
}

experience_invalid_id_response = {'detail': 'Not found.'}

update_experience_valid = {
    "company": "Some Company 5 update",
    "position": "Backend Developer update",
    "start": "2014-02-26",
    'end': "2018-02-26",
    'description': 'New description'
}

update_experience_valid_response = {
    'id': 5,
    "company": "Some Company 5 update",
    "position": "Backend Developer update",
    "start": "2014-02-26",
    'end': "2018-02-26",
    'description': 'New description',
    "candidate": 1
}