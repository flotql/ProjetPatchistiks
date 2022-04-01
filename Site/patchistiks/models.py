from django.db import models

# Create your models here.


class Spell(models.Model):
    spellName = models.CharField(max_length=50)
    spellEffect = models.CharField(max_length=500)