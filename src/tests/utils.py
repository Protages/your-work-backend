from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


def get_superuser_access_token() -> str:
    '''Create superuser for tests or create mvp db, return `access_token`.'''
    superuser = User.objects.create_superuser(
        email='superuser@mail.com', password='superuserpass'
    )
    token = RefreshToken.for_user(superuser)
    return str(token.access_token)
