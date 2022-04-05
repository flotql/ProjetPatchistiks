from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class ItemType (models.Model):
    itemTypeName = models.CharField(max_length=50)

    def __str__(self):
        return self.itemTypeName

class ItemClass(models.Model):
    itemClassRarity = models.CharField(max_length=50)

    def __str__(self):
        return self.itemClassRarity

class Items(models.Model):
    itemName = models.CharField(max_length=50)
    chose = models.ManyToManyField(User)
    got = models.ManyToManyField(ItemType)


    def __str__(self):
        return self.itemName

class RoleChamp(models.Model):
    roleType = models.CharField(max_length=30)

    def __str__(self):
        return self.roleType

class Spell(models.Model):
    spellName = models.CharField(max_length=30)
    spellBind = models.CharField(max_length=2)

    def __str__(self):
        return self.spellName

class Champions(models.Model):
    championName = models.CharField(max_length=30)
    championTitle = models.CharField(max_length=50)
    are = models.ForeignKey(RoleChamp, on_delete=models.CASCADE)
    use = models.ForeignKey(Spell, on_delete=models.CASCADE)
    pick = models.ManyToManyField(User)

    def __str__(self):
        return self.championName

class Effect (models.Model):
    effectText = models.CharField(max_length=300, blank=True)
    effectMake = models.ManyToManyField(Items, through='Make')
    get = models.ManyToManyField(Spell)

    def __str__(self):
        return self.effectText

class Patch(models.Model):
    patchNumber = models.CharField(max_length=20)
    patchDate = models.DateTimeField('Date de publication')

    def __str__(self):
        return self.patchNumber, self.patchDate

class Stats(models.Model):
    statName = models.CharField(max_length=50)
    statValue = models.IntegerField(default=0)
    will = models.ManyToManyField(Items)
    modify = models.ManyToManyField(Patch, through='Affect')
    have = models.ManyToManyField(Champions)
    put = models.ManyToManyField(Effect)

    def __str__(self):
        return self.statName, self.statValue

class Affect(models.Model):
    affectStat = models.DecimalField(max_digits=5, decimal_places=3)
    stat = models.ForeignKey(Stats, on_delete=models.CASCADE)
    patch = models.ForeignKey(Patch, on_delete=models.CASCADE)

    def __str__(self):
        return self.affectStat

class Make(models.Model):
    makeText = models.CharField(max_length=500)
    makeEffect = models.ForeignKey(Effect, on_delete=models.CASCADE, null=True)
    makeItems = models.ForeignKey(Items, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.makeText