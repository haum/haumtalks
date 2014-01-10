# -*- encoding:utf8 -*-
from django.shortcuts import render_to_response, get_object_or_404

from talksplanning.models import Batch, Talk, Hacker
from talksplanning.forms import TalkProposalForm

def home(request):
    """ Homepage """

    batches = Batch.objects.filter(published=True)

    return render_to_response('home.html', {'batches':batches})

def batch_detail(request, id):
    """ Details à propos d'un batch """

    batch = get_object_or_404(Batch, pk=id)
    talks = batch.talk_set.all()
    auditeurs = batch.participants.filter(hackerbatch__auditeur=True)

    return render_to_response('batch_detail.html', {'batch':batch, 'talks':talks, 'auditeurs':auditeurs})

def batch_form(request, batch_id):
    """ Formulaire inscription à un talk """

    batch = get_object_or_404(Batch, pk=batch_id)

    return render_to_response('batch_form.html', {'batch':batch})

def talk_form(request, batch_id):
    """ Formulaire inscription à un talk """

    batch = get_object_or_404(Batch, pk=batch_id)
    form = TalkProposalForm()
    return render_to_response('talk_form.html', {'batch':batch, 'form': form})


def add_talk(request, batch_id):
    """ Ajoute un talk à un batch """
    pass



