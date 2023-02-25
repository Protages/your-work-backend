'''Data for canditate endpoint tests'''

from app.models import Candidate


create_canditate_valid = [
    {  # Max data
        "email": "canditate_1@mail.com",
        "password": "canditate1pass",
        "first_name": "Canditate1First",
        "last_name": "Canditate1Last",
        "sex": Candidate.NOT_CHOISEN,
        "birthday": "2000-02-24",
        "position": "Python developer",
        "status": Candidate.SEARCH,
        "salary": 100000,
        "education": "some_education1",
        "skills": "some_skills1",
        "about": "Canditate 1 about",
        "contact_email": "canditate_1_contact@mail.com",
        "phone": "+79000000123",
        "tg": "https://t.me/canditate1",
        "city": "Moscow"
    },
    {  # Min data
        "email": "canditate_2@mail.com",
        "password": "canditate2pass",
        "first_name": "Canditate2First",
        "last_name": "Canditate2Last",
        "position": "Java developer",
    },
    {  # Min data
        "email": "canditate_3@mail.com",
        "password": "canditate3pass",
        "first_name": "Canditate3First",
        "last_name": "Canditate3Last",
        "position": "Golang developer",
    },
    {  # Min data
        "email": "canditate_4@mail.com",
        "password": "canditate4pass",
        "first_name": "Canditate4First",
        "last_name": "Canditate4Last",
        "position": "C# developer",
    },
    {  # Min data
        "email": "canditate_5@mail.com",
        "password": "canditate5pass",
        "first_name": "Canditate5First",
        "last_name": "Canditate5Last",
        "position": "C developer",
    }
]

canditate_valid_reponse = [
    {
        'id': 1,
        "email": "canditate_1@mail.com",
        "first_name": "Canditate1First",
        "last_name": "Canditate1Last",
        "sex": Candidate.NOT_CHOISEN,
        "birthday": "2000-02-24",
        "position": "Python developer",
        "status": Candidate.SEARCH,
        "salary": 100000,
        "education": "some_education1",
        "skills": "some_skills1",
        "about": "Canditate 1 about",
        "contact_email": "canditate_1_contact@mail.com",
        "phone": "+79000000123",
        "tg": "https://t.me/canditate1",
        "city": "Moscow"
    },
    {
        'id': 2,
        "email": "canditate_2@mail.com",
        "first_name": "Canditate2First",
        "last_name": "Canditate2Last",
        "sex": Candidate.NOT_CHOISEN,
        "birthday": None,
        "position": "Java developer",
        "status": Candidate.SEARCH,
        "salary": None,
        "education": None,
        "skills": None,
        "about": None,
        "contact_email": "canditate_2@mail.com",
        "phone": None,
        "tg": None,
        "city": None
    },
    {
        'id': 3,
        "email": "canditate_3@mail.com",
        "first_name": "Canditate3First",
        "last_name": "Canditate3Last",
        "sex": Candidate.NOT_CHOISEN,
        "birthday": None,
        "position": "Golang developer",
        "status": Candidate.SEARCH,
        "salary": None,
        "education": None,
        "skills": None,
        "about": None,
        "contact_email": "canditate_3@mail.com",
        "phone": None,
        "tg": None,
        "city": None
    },
    {
        'id': 4,
        "email": "canditate_4@mail.com",
        "first_name": "Canditate4First",
        "last_name": "Canditate4Last",
        "sex": Candidate.NOT_CHOISEN,
        "birthday": None,
        "position": "C# developer",
        "status": Candidate.SEARCH,
        "salary": None,
        "education": None,
        "skills": None,
        "about": None,
        "contact_email": "canditate_4@mail.com",
        "phone": None,
        "tg": None,
        "city": None
    },
    {
        'id': 5,
        "email": "canditate_5@mail.com",
        "first_name": "Canditate5First",
        "last_name": "Canditate5Last",
        "sex": Candidate.NOT_CHOISEN,
        "birthday": None,
        "position": "C developer",
        "status": Candidate.SEARCH,
        "salary": None,
        "education": None,
        "skills": None,
        "about": None,
        "contact_email": "canditate_5@mail.com",
        "phone": None,
        "tg": None,
        "city": None
    },
]

create_canditate_invalid_password = {
    "email": "user_999@mail.com",
    "password": "small",  # invalid
    "first_name": "User999First",
    "last_name": "User999Last",
    "position": "Python developer",
}

create_canditate_invalid_password_reponse = {
    'password': [
        'This password is too short. It must contain at least 8 characters.'
    ]
}

create_canditate_invalid_required = {
    "email": "user_999@mail.com",
    "password": "user1pass",
}

create_canditate_invalid_required_reponse = {
    'first_name': ['This field is required.'],
    'last_name': ['This field is required.'],
    'position': ['This field is required.']
}

create_canditate_invalid_unique = [
    {
        "email": "canditate_1@mail.com",  # alredy exist in user-candidate
        "password": "canditate999pass",
        "first_name": "Canditate999First",
        "last_name": "Canditate999Last",
        "position": "Python developer",
    },
    {
        "email": "company_1@mail.com",  # alredy exist in user-company
        "password": "canditate999pass",
        "first_name": "Canditate999First",
        "last_name": "Canditate999Last",
        "position": "Python developer",
    },
]

create_canditate_invalid_unique_reponse = {'email': ['This field must be unique.']}

candidate_invalid_id_response = {'detail': 'Not found.'}

update_canditate_valid = {
    "first_name": "Canditate5FirstUpdate",
    "last_name": "Canditate5LastUpdate",
    "sex": Candidate.MAN,
    "birthday": '1999-12-12',
    "position": "C++ developer",
    "status": Candidate.NOT_SEARCH,
    "salary": 500000,
    "education": 'some_education',
    "skills": 'skills',
    "about": 'New about',
    "contact_email": "canditate_5_update@mail.com",
    "phone": '+79000000011',
    "tg": "https://t.me/canditate5",
    "city": "Moscow"
}

update_canditate_valid_response = {
    'id': 5,
    'email': 'canditate_5@mail.com',
    "first_name": "Canditate5FirstUpdate",
    "last_name": "Canditate5LastUpdate",
    "sex": Candidate.MAN,
    "birthday": '1999-12-12',
    "position": "C++ developer",
    "status": Candidate.NOT_SEARCH,
    "salary": 500000,
    "education": 'some_education',
    "skills": 'skills',
    "about": 'New about',
    "contact_email": "canditate_5_update@mail.com",
    "phone": '+79000000011',
    "tg": "https://t.me/canditate5",
    "city": "Moscow"
}