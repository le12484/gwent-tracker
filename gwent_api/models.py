from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(primary_key=True, max_length=120)


    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)

class Faction(models.Model):
    name = models.CharField(primary_key=True, max_length=120)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Group(models.Model):
    name = models.CharField(primary_key=True, max_length=120)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Rarity(models.Model):
    name = models.CharField(primary_key=True, max_length=120)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Position(models.Model):
    name = models.CharField(primary_key=True, max_length=120)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class CardSet(models.Model):
    name = models.CharField(primary_key=True, max_length=120)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Variation(models.Model):
    
    availability = models.ForeignKey(CardSet)
    rarity = models.ForeignKey(Rarity)

    def __unicode__(self):
        return '%s - %s' % (self.availability, self.rarity)

    def __str__(self):
        return '%s - %s' % (self.availability, self.rarity)


class Card(models.Model):
    categories = models.ManyToManyField(Category)
    faction = models.ForeignKey(Faction)
    group = models.ForeignKey(Group)
    rarity = models.ForeignKey(Rarity)
    flavor = models.TextField(max_length=1200)
    info = models.TextField(max_length=1200)
    art = models.TextField(max_length=1200)
    name = models.CharField(primary_key=True, max_length=120)
    positions = models.ManyToManyField(Position)
    availability = models.ForeignKey(CardSet)


    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)
