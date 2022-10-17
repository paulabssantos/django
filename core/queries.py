from core import models

def all_states():
    return models.State.objects.all()
