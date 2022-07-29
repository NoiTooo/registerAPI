from ast import Or
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from datetime import datetime
import os
import uuid
import hashlib
from PIL import Image


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is must')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


""" User """

# hash images


def _user_profile_avator_upload_to(instance, filename):
    current_time = datetime.now()
    pre_hash_name = '%s%s%s' % (instance.id, filename, current_time)
    extension = str(filename).split('.')[-1]
    hs_filename = '%s.%s' % (hashlib.md5(
        pre_hash_name.encode()).hexdigest(), extension)
    saved_path = 'images/users/'
    return '%s%s' % (saved_path, hs_filename)


# varidation


def validate_is_picture(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ['.jpg', '.png', '.jpeg']:
        raise ValidationError('"jpg",".png","jpeg"のみ可能です」')


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    userimage = models.ImageField(upload_to=_user_profile_avator_upload_to,
                                  default='images/default_icon.png', validators=[validate_is_picture], blank=True, null=True)
    follows = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='myfollows')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    # Resizing Images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.userimage.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.userimage.path)

    def __str__(self):
        return self.email


class Organization(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    users = models.ManyToManyField(User, related_name='organizations_users')

    def __str__(self):
        return self.name
