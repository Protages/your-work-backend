from django.urls import reverse
from django.shortcuts import redirect


def redirect_to_docs(request):
    return redirect(to=reverse('schema-swagger-ui'))
