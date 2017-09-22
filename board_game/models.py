# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Type(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
         return self.name

class Mechanisms(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
         return self.name

class Category(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
         return self.name

class Games(models.Model):
      name = models.CharField(max_length=100)
      players = models.CharField(max_length=50)
      playing_time = models.CharField(max_length=50)
      description = models.CharField(max_length=500)
      links = models.CharField(max_length=100)
      own = models.BooleanField
      pnp = models.BooleanField
      type = models.ForeignKey(Type, on_delete=models.CASCADE)
      mechanisms = models.ForeignKey(Mechanisms, on_delete=models.CASCADE)
      category = models.ForeignKey(Category, on_delete=models.CASCADE)

      def __str__(self):
         return self.name

