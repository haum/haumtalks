# -*- encoding:utf8 -*-
from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from talksplanning.models import Batch, Talk, Hacker
from talksplanning.forms import TalkProposalForm, ListenerForm

def home(request):
    """ Homepage """

    batches = Batch.objects.filter(published=True)

    return render_to_response('home.html', {'batches':batches})

def batch_detail(request, id):
    """ Details à propos d'un batch """

    batch = get_object_or_404(Batch, pk=id)
    talks = batch.talk_set.all()
    auditeurs = batch.participants.filter(hackerbatch__auditeur=True)
    form = ListenerForm()

    return render_to_response('batch_detail.html',
                              {
                                  'batch':batch,
                                  'talks':talks,
                                  'auditeurs':auditeurs,
                                  'form':form},
                             context_instance=RequestContext(request))

def batch_form(request, batch_id):
    """ Formulaire inscription à un talk """

    batch = get_object_or_404(Batch, pk=batch_id)

    if request.method == 'POST':
        f = ListenerForm(request.POST)
        if not f.is_valid():
            return render_to_response('batch_detail.html', {'batch':batch, 'form': f}, context_instance=RequestContext(request))
        else:
            listener = f.save(batch)
            return HttpResponseRedirect(reverse('batch_detail', args=(batch.id,)))
    else:
        return HttpResponseRedirect(reverse('batch_detail', args=(batch.id,)))

def talk_form(request, batch_id):
    """ Formulaire inscription à un talk """

    batch = get_object_or_404(Batch, pk=batch_id)

    if request.method == 'POST':
        f = TalkProposalForm(request.POST)
        if not f.is_valid():
            return render_to_response('talk_form.html', {'batch':batch, 'form': f}, context_instance=RequestContext(request))
        else:
            talks = f.save(batch)
            return HttpResponseRedirect(reverse('batch_detail', args=(batch.id,)))
    else:
        form = TalkProposalForm()
        return render_to_response('talk_form.html', {'batch':batch, 'form': form}, context_instance=RequestContext(request))


def add_talk(request, batch_id):
    """ Ajoute un talk à un batch """
    pass



