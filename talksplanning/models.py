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
    published = models.BooleanField("Publié", default=True)
    interne = models.BooleanField(default=False)

    responsable = models.ForeignKey(User)
    participants = models.ManyToManyField('Hacker', through='HackerBatch')

    # internal help texts
    published.help_text = "Un batch peut exister mais ne plus être publié"
    interne.help_text = "Si coché, le batch n'apparait pas sur les pages publiques (il est réservé aux membres du HAUM)"

    def __unicode__(self):
        return self.theme


class Talk(models.Model):
    """
    Talk, avec toutes les infos qui vont bien
    """

    titre = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField("URL", max_length=200, null=True, blank=True)

    # modération
    approved = models.BooleanField("Approuvé", default=False)

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
    haum = models.BooleanField(default=False, blank=True)

    # names for forms
    pseudo.verbose_name = "nom/pseudonyme"
    mail.verbose_name = "adresse e-mail"
    haum.verbose_name = "membre du HAUM"

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
