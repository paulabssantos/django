from unicodedata import name
from core import models

def all_states():
    return models.State.objects.all()

def update_state():
    return models.State.objects.filter(name__iexact='amazonas').update(name='Pará',abbreviation='PA')