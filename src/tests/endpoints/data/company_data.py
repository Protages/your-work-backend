'''Data for company endpoint tests'''


create_company_valid = [
    {
        "email": "company_1@mail.com",
        "password": "company1pass",
        "title": "Best company",
        "employees": 50,
        "city": "Moscow",
        "address": "some_address",
        'contact_email': 'company_1_contact@mail.com',
        "site": "http://company1.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_1",
        "about": "Company 1 about"
    },
    {
        "email": "company_2@mail.com",
        "password": "company2pass",
        "title": "Roga i Kopita",
        "employees": 100,
        "city": "Sent-Petersburg",
        "address": "some_address",
        "site": "http://company2.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_2",
        "about": "Company 2 about"
    },
    {
        "email": "company_3@mail.com",
        "password": "company3pass",
        "title": "Sberbank",
        "employees": 200,
        "city": "Ekaterenburg",
        "address": "some_address",
        "site": "http://company3.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_3",
        "about": "Company 3 about"
    },
    {
        "email": "company_4@mail.com",
        "password": "company1pass",
        "title": "Tinkoff",
        "employees": 400,
        "city": "Krasnodar",
        "address": "some_address",
        "site": "http://company4.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_4",
        "about": "Company 4 about"
    },
    {
        "email": "company_5@mail.com",
        "password": "company5pass",
        "title": "Best company",
        "employees": 1000,
        "city": "Moscow",
        "address": "some_address",
        "site": "http://company5.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_5",
        "about": "Company 5 about"
    }
]

company_valid_reponse = [
    {
        'id': 1,
        "email": "company_1@mail.com",
        "title": "Best company",
        "employees": 50,
        "city": "Moscow",
        "address": "some_address",
        'contact_email': 'company_1_contact@mail.com',
        "site": "http://company1.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_1",
        "about": "Company 1 about"
    },
    {
        'id': 2,
        "email": "company_2@mail.com",
        "title": "Roga i Kopita",
        "employees": 100,
        "city": "Sent-Petersburg",
        "address": "some_address",
        'contact_email': 'company_2@mail.com',
        "site": "http://company2.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_2",
        "about": "Company 2 about"
    },
    {
        'id': 3,
        "email": "company_3@mail.com",
        "title": "Sberbank",
        "employees": 200,
        "city": "Ekaterenburg",
        "address": "some_address",
        'contact_email': 'company_3@mail.com',
        "site": "http://company3.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_3",
        "about": "Company 3 about"
    },
    {
        'id': 4,
        "email": "company_4@mail.com",
        "title": "Tinkoff",
        "employees": 400,
        "city": "Krasnodar",
        "address": "some_address",
        'contact_email': 'company_4@mail.com',
        "site": "http://company4.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_4",
        "about": "Company 4 about"
    },
    {
        'id': 5,
        "email": "company_5@mail.com",
        "title": "Best company",
        "employees": 1000,
        "city": "Moscow",
        "address": "some_address",
        'contact_email': 'company_5@mail.com',
        "site": "http://company5.com/",
        "phone": "+79000000123",
        "tg": "https://t.me/company_5",
        "about": "Company 5 about"
    }
]

create_company_invalid_password = {
    "email": "company_999@mail.com",
    "password": "small",  # invalid
    "title": "Company 999",
    "employees": 100,
    "city": "City 999",
    "address": "some_address",
    "site": "http://company999.com/",
    "contact_email": "company999_contact@mail.com",
    "phone": "+79000000123",
    "tg": "https://t.me/company_999",
    "about": "Company 999 about"
}

create_company_invalid_password_reponse = {
    'password': [
        'This password is too short. It must contain at least 8 characters.'
    ]
}

create_company_invalid_required = {
    "email": "company999@mail.com",
    "password": "company1pass",
}

create_company_invalid_required_reponse = {
    'title': ['This field is required.'], 
    'employees': ['This field is required.'], 
    'city': ['This field is required.'], 
    'about': ['This field is required.']
}

create_company_invalid_unique = {
    "email": "company_1@mail.com",  # alredy exist
    "password": "company999pass",
    "title": "Company 999",
    "employees": 100,
    "city": "City 999",
    "address": "some_address",
    "site": "http://company999.com/",
    "contact_email": "company999_contact@mail.com",
    "phone": "+79000000123",
    "tg": "https://t.me/company_999",
    "about": "Company 999 about"
}

create_company_invalid_unique_reponse = {'email': ['This field must be unique.']}

company_invalid_id_response = {'detail': 'Not found.'}

update_company_valid = {
    "title": "Best company update",
    "employees": 1500,
    "city": "Ekaterenburg",
    "address": "some_address_update",
    "contact_email": "company_5_contact_update@mail.com",
    "site": "http://company5update.com/",
    "phone": "+79000000321",
    "tg": "https://t.me/company_5_update",
    "about": "Company 5 about update"
}

update_company_valid_response = {
    'id': 5,
    "email": "company_5@mail.com",
    "title": "Best company update",
    "employees": 1500,
    "city": "Ekaterenburg",
    "address": "some_address_update",
    "contact_email": "company_5_contact_update@mail.com",
    "site": "http://company5update.com/",
    "phone": "+79000000321",
    "tg": "https://t.me/company_5_update",
    "about": "Company 5 about update"
}