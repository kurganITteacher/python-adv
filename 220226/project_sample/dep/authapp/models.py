from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class KpkUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, email, password, **extra_fields):
        """
        Create and save a user with the given login, email, and password.
        """
        if not login:
            raise ValueError('The given login must be set')
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, email, password, **extra_fields)

    def create_superuser(self, login, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(login, email, password, **extra_fields)


class KpkUser(AbstractUser):
    objects = KpkUserManager()

    username = None

    login = models.CharField(
        'login',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': "A user with that login already exists.",
        },
    )
    d_birth = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatars',
                               blank=True)

    USERNAME_FIELD = 'login'
