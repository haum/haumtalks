# -*- coding:utf8 -*-

from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory

from talksplanning.models import Talk, Hacker

class TalkProposalForm(forms.ModelForm):
    """ Form to propose a talk """

    class Meta:
        model = Talk
        fields = ['titre', 'description', 'url']

    hacker_name = forms.CharField()
    hacker_mail = forms.EmailField()
    hacker_haum = forms.BooleanField()
    


