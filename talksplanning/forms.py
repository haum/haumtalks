# -*- coding:utf8 -*-

from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory

from talksplanning.models import Talk, Hacker, HackerBatch

class TalkProposalForm(forms.ModelForm):
    """ Form to propose a talk """

    class Meta:
        model = Talk
        fields = ['titre', 'description', 'url']

    hacker_name = forms.CharField()
    hacker_mail = forms.EmailField()
    hacker_haum = forms.BooleanField(required=False)

    def save(self, batch):

        # shorter is better
        cd = self.cleaned_data

        # == Hacker creation ==
        # 0 indice to get the Hacker instance
        speaker = Hacker.objects.get_or_create(
            pseudo = cd['hacker_name'],
            mail = cd['hacker_mail'],
            haum = cd['hacker_haum']
        )[0]
        batch = batch

        # == Talk ==
        talk = Talk()
        talk.titre = cd['titre']
        talk.description = cd['description']
        talk.url = cd.get('url') # may be None
        talk.speaker = speaker
        talk.batch = batch
        talk.save()

        # == Link Hacker <-> Batch ==
        HackerBatch(orateur=True, batch=batch, hacker=speaker).save()

        return talk
