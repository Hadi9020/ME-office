from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Member

def index(request):

    context = {
        "members": Member.objects.all().order_by('-register_date'),
    }

    return render(request, 'members/index.html', context)

def search(request, target):

    results = Member.objects.filter(
        Q(first_name__icontains=target) |
        Q(last_name__icontains=target) |
        Q(user_name__icontains=target) |
        Q(mle__icontains=target)
    ).order_by('-register_date')

    context = {
        "members": results,
        "query": target,
    }

    return render(request, 'members/search.html', context)

def profile(request, pk):

    context = {
        "member": get_object_or_404(Member, pk=pk),
    }

    return render(request, 'members/profile.html', context)
