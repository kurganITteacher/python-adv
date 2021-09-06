from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    # phone_validator = PhoneValidator()

    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_CHOICES = (
        (GENDER_MALE, _('male')),
        (GENDER_FEMALE, _('female')),
    )

    date_birth = models.DateField(_('birth date'), null=True)
    # phone_number = models.CharField(validators=[phone_validator],)
    gender = models.CharField(_('gender'), max_length=1,
                              choices=GENDER_CHOICES, blank=True)
