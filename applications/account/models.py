from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from applications.tasks.models import Task


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,  fullname, email, password, *args, **kwargs):
        fullname = models.CharField(max_length=50)
        email = self.normalize_email(email)
        user = self.model(fullname=fullname, email=email)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, *args, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = None
    fullname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='users_photo', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    favorite = models.ManyToManyField(Task, related_name='favorite', blank=True)

    def __str__(self):
        return self.user.email

    def create_activation_code(self):
        import hashlib
        string_to_encode = self.email + str(self.id)
        encode_string = string_to_encode.encode()
        md5_object = hashlib.md5(encode_string)
        # хранится хешированный код каждого пользователя
        activation_code = md5_object.hexdigest()
        self.activation_code = activation_code


