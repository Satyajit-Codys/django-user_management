from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, address, username, password, **extra_fields):
        if not email: 
            raise ValueError("Email must be proided")
        if not password: 
            raise ValueError("Password must be proided")
        
        user = self.model(
            email = self.normalize_email(email),
            address = address,
            username = username,
            
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

    def create_user(self,email,address,username,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,address,username,password,**extra_fields)
        
    def create_superuser(self, email,address,username,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email,address,username,password,**extra_fields)

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(db_index= True, unique=True,max_length=254)
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=240)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'address']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'