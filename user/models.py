from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=email, 
            nickname = nickname
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
        max_length=30,
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
    REQUIRED_FIELD = ['nickname',]

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
