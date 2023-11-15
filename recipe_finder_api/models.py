from datetime import date
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse


class CustomUserManager(UserManager):
    def create_user(self, username: str, email: str, password: str, birthday, name: str):
        """
        Create and save a user with the given username, email, password, name  birthday, profile_picture.
        """
        if not email:
            raise ValueError('The given email must be set')

        if not password:
            raise ValueError('The given password must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, name=name, birthday=birthday)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
def nameFile(instance, filename):
    todays_date = date.today()
    return '/'.join(['images', 'profile_picture', '{}'.format(todays_date), filename])

class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=100, blank=False, null=False, unique=True, error_messages={'unique': 'Please use another username'})
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True, error_messages={'unique': 'Please use another email for this user'})
    password = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    profile_picture = models.ImageField(upload_to=nameFile, default='not-image.png', null=True)
    birthday = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def get_email_field(self):
        return self.email
    

    def get_name(self):
        return self.name
    
    def __str__(self): 
        return "{}: {}, {}, {}".format(self.pk, self.username, self.email, self.name)
    

    objects = CustomUserManager()

    class Meta:
        db_table = "AuthUser"