# Create your views here.

from agenda.models import Contato
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'contatos': Contato.objects.all()[:5]
    })

def view_contato(request, nome):
    return render_to_response('view_contato.html', {
        'contato': get_object_or_404(Contato, nome=nome)
    })
