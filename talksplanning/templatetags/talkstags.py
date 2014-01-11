# -*- coding:utf8 -*-

from django import template

from talksplanning.models import Talk, Batch

register = template.Library()

@register.inclusion_tag('batch_listtag.html')
def batch_list():
    batches = Batch.objects.filter(published=True, interne=False)
    return {'batches': batches}



