from django.forms import models

from card.models import Card


class CardForm(models.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'