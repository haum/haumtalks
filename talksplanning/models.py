# -*- encoding:utf8 -*-
from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    """
    Batch of talks (session)
    """

    theme = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    published = models.BooleanField(default=True)
    interne = models.BooleanField(default=False)

    responsable = models.ForeignKey(User)
    participants = models.ManyToManyField('Hacker', through='HackerBatch')

    def __unicode__(self):
        return self.theme


class Talk(models.Model):
    """
    Talk, avec toutes les infos qui vont bien
    """

    titre = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()

    speaker = models.ForeignKey('Hacker')
    batch = models.ForeignKey('Batch')

    def __unicode__(self):
        return self.titre


class Hacker(models.Model):
    """
    Hacker (vaillant rien d'impossible)
    """

    pseudo = models.CharField(max_length=50)
    mail = models.EmailField()
    haum = models.BooleanField(default=False)

    def __unicode__(self):
        return self.pseudo


class HackerBatch(models.Model):
    """
    Meta data à propos de la liaison batch -> hacker
    """

    auditeur = models.BooleanField(default=True)
    orateur = models.BooleanField(default=False)

    batch = models.ForeignKey('Batch')
    hacker = models.ForeignKey('Hacker')
