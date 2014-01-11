# -*- coding: utf8 -*-
from django.contrib import admin

from talksplanning.models import Batch, Talk, Hacker

class BatchAdmin(admin.ModelAdmin):

    list_display = ('theme', 'responsable', 'date', 'published', 'interne')
    list_filter = ('published', 'interne', 'responsable')
    list_editable = ('published', 'interne')
    ordering = ['date']

    fieldsets = (
        (None,      {'fields': ['theme', 'responsable', 'description']}),
        ('Date',    {'fields': ['date']}),
        ('Visibilité', {'fields': ['published', 'interne']})
    )

class HackerAdmin(admin.ModelAdmin):

    list_display = ('pseudo', 'mail', 'batches_count', 'haum')
    ordering = ['pseudo']


class TalkAdmin(admin.ModelAdmin):

    list_display = ('titre', 'speaker', 'batch', 'url', 'approved')
    list_filter = ('approved', 'batch', 'speaker')
    list_editable = ('approved',)

admin.site.register(Batch, BatchAdmin)
admin.site.register(Hacker, HackerAdmin)
admin.site.register(Talk, TalkAdmin)
