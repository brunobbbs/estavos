# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    bio = models.TextField(blank=True)
    birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()