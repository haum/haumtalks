# -*- encoding:utf8 -*-
from django.db import models
from django.contrib.auth.models import User

from haumevents.models import Hacker


class Event(models.Model):
    """
    Event
    """

    # Données de table
    titre = models.CharField(max_length=200)
    description = models.TextField()
    description = models.TextField()
    published = models.BooleanField("Publié", default=True)
    interne = models.BooleanField(default=False)
    programme = models.BooleanField('Programmé', default=True)

    # Données externes
    dates = models.OneToManyField('Date')
    responsable = models.ForeignKey(User)
    participants = models.ManyToManyField('Hacker', through='HackerEvent')

    # internal help texts
    published.help_text = "Un event peut exister mais ne plus être publié"
    interne.help_text = "Si coché, le event n'apparait pas sur les pages publiques (il est réservé aux membres du HAUM)"
    programme.help_text = "Si coché alors l'event est considéré \"Programmé\" (sa date est connue et affichée)"

    def __unicode__(self):
        return self.theme




class HackerEvent(models.Model):
    """
    Meta data à propos de la liaison event -> hacker
    """
    # Données de table
    staff = models.BooleanField(default=False)

    # Données externes
    event = models.ForeignKey('Event')
    hacker = models.ForeignKey('Hacker')

    def __unicode__(self):
        return self.hacker.__unicode__()+' <-> '+self.event.__unicode__()




