from django.shortcuts import render, redirect
from django.db.models import F
from django.views.generic import ListView

from card.models import Tipo, Card


def TipoList(request):
        data = {}
        data['tipos'] = Tipo.objects.all()
        return render(request, 'card/tipo_list.html', data)


def CriarCard(request):
        pk = request.POST.get('tipo')
        t = Tipo.objects.get(pk=pk)
        controle = Card.position_add(pk)
        descricao = request.POST.get('descricao')
        Card.objects.create(descricao=descricao, tipo=t, posicao=controle)
        return redirect('list')


def ExcluiCard(request, pk):
        card = Card.objects.get(pk=pk)
        card.delete()
        return redirect('list')


def UpdateCard(request, pk):
        card = Card.objects.get(pk=pk)
        descricao = request.POST.get('descricao')
        card.descricao = descricao
        card.save()
        return redirect('list')


def MudaPosicao(request, pk, tp):
        tipo = Tipo.objects.get(pk=tp)
        card = Card.objects.get(pk=pk)
        tipo.cards.filter(posicao__lt=card.posicao).update(posicao=F('posicao')+1)
        card.posicao = 1
        card.save()
        return redirect('list')


def MudaTipo(request):
        idcard = request.POST.get('modalcard')
        btn = request.POST.get('btntipomuda')
        card = Card.objects.get(pk=idcard)
        tipo = Tipo.objects.filter(nome=btn)[0]
        card.tipo = tipo
        card.posicao = Card.position_add(tipo.id)
        card.save()
        return redirect('list')


def CriarTipo(request):
        nome = request.POST.get('descricao')
        Tipo.objects.create(nome=nome)
        return redirect('list')


def ExcluiTipo(request, pk):
        tipo = Tipo.objects.get(pk=pk)
        tipo.delete()
        return redirect('list')
