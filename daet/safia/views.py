from django.shortcuts import render
from .models import *

# Create your views here.
from .sevices import search_recipe


def index(request):
    ctgs = Category.objects.all()
    news = Recipe.objects.all().order_by("-pk")
    ctx = {
        'ctgs': ctgs,
        'news': news
    }
    return render(request, 'index.html', ctx)


def about(request):
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(request, 'about.html', ctx)


def blog(request):
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(request, 'blog-post.html', ctx)


def elements(request):
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(request, 'elements.html', ctx)


def contact(request):
    ctgs = Category.objects.all()

    if request.POST:
        sugest = Suggestion()
        sugest.name = request.POST.get('name')
        sugest.number = request.POST.get('number')
        sugest.subject = request.POST.get('subject')
        sugest.message = request.POST.get('message')
        sugest.save()

    ctx = {
        'ctgs': ctgs
    }
    return render(request, 'contact.html', ctx)


def recipe(request, pk):
    retseplar = Recipe.objects.get(pk=pk)
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs,
        'retseplar': retseplar
    }
    return render(request, 'recipe.html', ctx)


def category(requests, slug=None):
    ctgs = Category.objects.all()
    recipes = None
    ctg = None
    search = None
    if requests.GET and requests.GET.get('search', None):
        search = requests.GET.get('search', None)
        recipes = search_recipe(search)

    if slug:
        ctg = Category.objects.get(slug=slug)
        recipes = Recipe.objects.filter(ctg=ctg).order_by("-pk")

    ctx = {
        'ctgs': ctgs,
        'recipes': recipes,
        'ctg': ctg,
        'search': search,
        'leng': len(recipes) if recipes else 0 if search else len(ctgs)}

    return render(requests, 'category.html', ctx)
