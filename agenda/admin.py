from django.contrib import admin
from agenda.models import Contato


class AgendaAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'nome': ('nome',)}


admin.site.register(Contato)