# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(
        max_length=255,
    )
    apellido = models.CharField(
        max_length=255,
    )
    email = models.EmailField()

    Telefono =models.CharField(
        max_length=255,
    )
    Direccion =models.CharField(
        max_length=255,
    )

    def __str__(self):

        return ' '.join([
            self.nombre,
            self.apellido,
            self.Telefono,
        ])