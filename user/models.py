from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import MinLengthValidator

USER_NICKNAME_LENGTH_RANGE = (4, 15)

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not nickname:
            raise ValueError("Users must have a nickname")

        user = self.model(
            email=self.normalize_email(email), 
            nickname = nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """
    유저 모델 정의
    """
    email = models.EmailField(
        verbose_name='Email Address',
        unique=True,
    )

    nickname = models.CharField(
        verbose_name='Nickname',
        validators=[
            MinLengthValidator(USER_NICKNAME_LENGTH_RANGE[0]),
        ], 
        max_length=USER_NICKNAME_LENGTH_RANGE[1],
        unique=True
    )

    is_active = models.BooleanField(
        verbose_name='Is active',
        default=True
    )
    
    is_admin = models.BooleanField(
        verbose_name='Is admin',
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    objects = UserManager()

    def __str__(self):
        return f'{self.nickname} - {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "USER"
