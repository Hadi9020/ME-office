from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Case, When, Value, IntegerField
from .models import News

def index(request):
    context = {
        "news": News.objects.all().order_by('-created_at'),
    }
    return render(request, 'news/index.html', context)

def search(request, target):

    results = News.objects.annotate(
        rank=Case(
            When(title__icontains=target, then=Value(4)),
            When(text__icontains=target, then=Value(3)),
            When(tags__name__icontains=target, then=Value(2)),
            When(author__username__icontains=target, then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        )
    ).filter(rank__gt=0).order_by('-rank', '-created_at')

    context = {
        "news": results,
        "query": target,
    }
    return render(request, 'news/search.html', context)

def news_detail(request, pk):

    news_item = get_object_or_404(News, pk=pk)
    context = {
        "news": news_item,
    }
    return render(request, 'news/news.html', context)
