import pytest

from django.conf import settings
from rest_framework.test import APIClient
from django.test.utils import setup_databases, teardown_databases
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from tests.utils import get_superuser_access_token


@pytest.fixture(scope='session')
def django_db_modify_db_settings():
    '''Set new database settings. ATOMIC_REQUESTS required for pytest-django(?)'''

    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'testdb.sqlite3',
        'ATOMIC_REQUESTS': True
    }


@pytest.fixture(scope='session')
def django_db_setup(request, django_db_modify_db_settings, django_db_blocker) -> None:
    '''Create temporary database and after all tests teardown it'''

    with django_db_blocker.unblock():
        db_cfg = setup_databases(
            verbosity=request.config.option.verbose,
            interactive=False,
        )

    def teardown_database() -> None:
        with django_db_blocker.unblock():
            try:
                teardown_databases(db_cfg, verbosity=request.config.option.verbose)
            except Exception as exc:
                request.node.warn(
                    pytest.PytestWarning(
                        f"Error when trying to teardown test databases: {exc!r}"
                    )
                )
    request.addfinalizer(teardown_database)


@pytest.fixture(scope='session')
def db_no_rollback(request, django_db_setup, django_db_blocker) -> None:
    '''
    Fixture for providing test access to django
    database without recovery database after each test
    '''

    django_db_blocker.unblock()
    request.addfinalizer(django_db_blocker.restore)


@pytest.fixture(scope='session')
def api_client(db_no_rollback):
    '''
    `APIClient` with header `HTTP_AUTHORIZATION=Bearer superuser_access_token`
    for access to all endpoints.
    '''
    access_token = get_superuser_access_token()
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
    yield client


@pytest.fixture(scope='session')
def api_client_without_access_token(db_no_rollback):
    yield APIClient()
