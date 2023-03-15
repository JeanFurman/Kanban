from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=40, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

    def testeField(self):
        return self.cards.exists()


class Card(models.Model):
    descricao = models.CharField(max_length=40)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='cards')
    posicao = models.IntegerField()

    def __str__(self):
        return self.descricao

    def position_add(controle):
        tipo = Tipo.objects.get(pk=controle)
        maior = tipo.cards.all().order_by('posicao').last()
        if not maior:
            return 1
        return maior.posicao + 1


