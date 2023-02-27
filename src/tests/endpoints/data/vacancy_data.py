'''Data for vacancy endpoint tests'''

from django.conf import settings


create_vacancy_valid = [
    {  # Max data
        "title": "Python Middle developer",
        "salary": 170000,
        'required_experience': 2,
        "skills": "some_skills1",
        "description": "some_description1",
        "company": 1
    },
    {
        "title": "Python Junior developer",
        "salary": 80000,
        'required_experience': 1,
        "skills": "some_skills2",
        "description": "some_description2",
        "company": 1
    },
    {
        "title": "Java developer",
        "salary": 150000,
        'required_experience': 3,
        "skills": "some_skills3",
        "description": "some_description3",
        "company": 1
    },
    {  # Min data
        "title": "TeamLead",
        "salary": 300000,
        "skills": "some_skills4",
        "description": "some_description4",
        "company": 1
    },
    {
        "title": "React developer",
        "salary": 100000,
        "skills": "some_skills5",
        "description": "some_description5",
        "company": 1
    }
]

vacancy_valid_reponse = [
    {
        'id': 1,
        "title": "Python Middle developer",
        "salary": 170000,
        'required_experience': 2,
        "skills": "some_skills1",
        "description": "some_description1",
        "company": 1
    },
    {
        'id': 2,
        "title": "Python Junior developer",
        "salary": 80000,
        'required_experience': 1,
        "skills": "some_skills2",
        "description": "some_description2",
        "company": 1
    },
    {
        'id': 3,
        "title": "Java developer",
        "salary": 150000,
        'required_experience': 3,
        "skills": "some_skills3",
        "description": "some_description3",
        "company": 1
    },
    {
        'id': 4,
        "title": "TeamLead",
        "salary": 300000,
        'required_experience': None,
        "skills": "some_skills4",
        "description": "some_description4",
        "company": 1
    },
    {
        'id': 5,
        "title": "React developer",
        "salary": 100000,
        'required_experience': None,
        "skills": "some_skills5",
        "description": "some_description5",
        "company": 1
    }
]

create_vacancy_invalid_salary = [
    {
        "title": "React developer",
        "salary": settings.MIN_SALARY - 100,  # invalid
        "skills": "some_skills999",
        "description": "some_description999",
        "company": 1
    },
    {
        "title": "React developer",
        "salary": settings.MAX_SALARY + 100,  # invalid
        "skills": "some_skills999",
        "description": "some_description999",
        "company": 1
    }
]

create_vacancy_invalid_salary_response = [
    {
        'salary': [f'Too small value, min value {settings.MIN_SALARY}']
    },
    {
        'salary': [f'Too big value, max value {settings.MAX_SALARY}']
    }
]

create_vacancy_invalid_required = {
    "title": "Python Middle developer 999"
}

create_vacancy_invalid_required_reponse = {
    'salary': ['This field is required.'], 
    'skills': ['This field is required.'], 
    'description': ['This field is required.'], 
    'company': ['This field is required.']
}

create_vacancy_invalid_company_id = {
    "title": "React developer999",
    "salary": 100000,
    "skills": "some_skills999",
    "description": "some_description999",
    "company": 999
}

create_vacancy_invalid_company_id_reponse = {
    'company': ['Invalid pk "999" - object does not exist.']
}

vacancy_invalid_id_response = {'detail': 'Not found.'}

update_vacancy_valid = {
    "title": "Python Middle developer update",
    "salary": 90000,
    'required_experience': 1,
    "skills": "some_skills1_update",
    "description": "some_description1_update",
}

update_vacancy_valid_response = {
    'id': 5,
    "title": "Python Middle developer update",
    "salary": 90000,
    'required_experience': 1,
    "skills": "some_skills1_update",
    "description": "some_description1_update",
    "company": 1
}
