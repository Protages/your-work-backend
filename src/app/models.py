import os

from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

from app.storage import OverwriteStorage


def upload_to_vacancy(instance, filename: str):
    '''Specifies download path and file name'''
    extension = filename.split('.')[-1]
    filename = f'image.{extension}'
    return os.path.join('vacancies', str(instance.id), filename)


def upload_to_cv_file(instance, filename):
    '''Specifies download path and file name'''
    return os.path.join('responses', str(filename))


class Company(models.Model):
    title = models.CharField(verbose_name='company title', max_length=128)
    employees = models.IntegerField(verbose_name='count of employees')
    city = models.CharField(verbose_name='city', max_length=128)
    address = models.CharField(
        verbose_name='company address', max_length=512, null=True, blank=True
    )
    site = models.URLField(verbose_name='company site', null=True, blank=True)
    contact_email = models.EmailField(
        verbose_name='contact email', null=True, blank=True
    )
    phone = PhoneNumberField(
        verbose_name='company phone', 
        region=settings.PHONENUMBER_DEFAULT_REGION,
        null=True, blank=True
    )
    tg = models.URLField(verbose_name='telegram', null=True, blank=True)
    about = models.TextField(verbose_name='about company')

    def __str__(self) -> str:
        return self.title


class Vacancy(models.Model):
    title = models.CharField(verbose_name='title', max_length=128)
    salary = models.PositiveIntegerField(verbose_name='salary in rub')
    required_experience = models.PositiveSmallIntegerField(
        verbose_name='required years of experience', blank=True, null=True
    )
    skills = models.TextField(verbose_name='necessary skills')
    description = models.TextField('description')
    img = models.ImageField(
        verbose_name='image',
        upload_to=upload_to_vacancy,
        storage=OverwriteStorage,
        blank=True, null=True
    )
    company = models.ForeignKey(
        to=Company, 
        verbose_name='company', 
        on_delete=models.CASCADE, 
        related_name='vacancies'
    )

    def __str__(self) -> str:
        return self.title


class Candidate(models.Model):
    NOT_CHOISEN = 'NC'
    MAN = 'MN'
    WOMAN = 'WN'
    SEX = [
        (NOT_CHOISEN, 'Not choisen'),
        (MAN, 'Man'),
        (WOMAN, 'Woman')
    ]

    SEARCH = 'SC'
    NOT_SEARCH = 'NSC'
    THINK = 'TH'
    CANDIDATE_STATUS = [
        (SEARCH, 'In search of a job'),
        (NOT_SEARCH, 'Not looking for a job'),
        (THINK, 'Offered a job while Im thinking')
    ]

    first_name = models.CharField(verbose_name='first name', max_length=128)
    last_name = models.CharField(verbose_name='last name', max_length=128)
    sex = models.CharField(
        verbose_name='sex', choices=SEX, default=NOT_CHOISEN, max_length=8
    )
    birthday = models.DateField(verbose_name='birthday', null=True, blank=True)
    position = models.CharField(verbose_name='position', max_length=128)
    status = models.CharField(
        verbose_name='resume status',
        choices=CANDIDATE_STATUS,
        default=SEARCH,
        max_length=8
    )
    salary = models.PositiveIntegerField(
        verbose_name='salary', blank=True, null=True
    )
    education = models.TextField(verbose_name='education', blank=True, null=True)
    skills = models.TextField(verbose_name='skills', blank=True, null=True)
    about = models.TextField(verbose_name='about candidate', blank=True, null=True)
    contact_email = models.EmailField(
        verbose_name='contact email', blank=True, null=True
    )
    phone = PhoneNumberField(
        verbose_name='candidate phone',
        region=settings.PHONENUMBER_DEFAULT_REGION,
        blank=True, null=True
    )
    tg = models.URLField(verbose_name='telegram', blank=True, null=True)
    city = models.CharField(verbose_name='city', max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Experience(models.Model):
    company = models.CharField(verbose_name='company title', max_length=128)
    position = models.CharField(verbose_name='position in company', max_length=128)
    start = models.DateField(verbose_name='start of work')
    end = models.DateField(verbose_name='end of work', blank=True, null=True)
    description = models.TextField(verbose_name='description', blank=True, null=True)
    candidate = models.ForeignKey(
        to=Candidate,
        verbose_name='candidate',
        on_delete=models.CASCADE,
        related_name='experience'
    )

    def __str__(self) -> str:
        return f'{self.company} {self.position}'


class Reaction(models.Model):
    NOT_VIEWED = 'NVD'
    VIEWED = 'VD'
    INVITE = 'IV'
    REJECT = 'RJ'
    REACTION_STATUS = [
        (NOT_VIEWED, 'Not viewed'),
        (VIEWED, 'Viewed'),
        (INVITE, 'Invite'),
        (REJECT, 'Rejection')
    ]

    candidate = models.ForeignKey(
        to=Candidate,
        verbose_name='candidate',
        on_delete=models.SET_NULL,
        related_name='responses',
        null=True
    )
    vacancy = models.ForeignKey(
        to=Vacancy, 
        verbose_name='vacancy', 
        on_delete=models.SET_NULL, 
        related_name='responses',
        null=True
    )
    status = models.CharField(
        verbose_name='status', choices=REACTION_STATUS, default=NOT_VIEWED, max_length=8
    )
    comment = models.TextField(verbose_name='candidate comment', blank=True, null=True)
    cv = models.FileField(verbose_name='cv file', upload_to=upload_to_cv_file)

    class Meta:
        unique_together = ['candidate', 'vacancy']

    def __str__(self) -> str:
        return f'{self.pk}'
