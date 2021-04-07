from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Hero
from django.urls import reverse
# Create your views here.


def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    details = Hero.objects.get(pk=hero_id)
    context = {
        'details': details
    }
    return render(request, 'heroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Hero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catch_phrase=catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/create.html')


def edit(request, hero_id):
    if request.method == 'POST':
        details = Hero.objects.get(pk=hero_id)
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        details.name = name
        details.alter_ego = alter_ego
        details.primary_ability = primary_ability
        details.secondary_ability = secondary_ability
        details.catch_phrase = catch_phrase
        details.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        details = Hero.objects.get(pk=hero_id)
        context = {
            'details': details
        }
        return render(request, 'heroes/edit.html', context)



