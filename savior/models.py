# En tu_aplicacion/models.py

from django.db import models

class Prompt(models.Model):
    prompt = models.TextField()
