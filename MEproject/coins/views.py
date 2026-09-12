from django.shortcuts import render, get_object_or_404
from .models import Coin

def index(request):

    context = {
        "new1": "This part doesn't have any problem",
        "new2": "This part doesn't have any problem",
        "new3": "This part doesn't have any problem",
        "new4": "This part doesn't have any problem",
        "new5": "This part doesn't have any problem",
        "new6": "This part doesn't have any problem",
        "test": "This part doesn't have any problem",
    }

    return render(request, 'coin/index.html', context)

def self(request, user_id):

    context = {
        "new1": "This part doesn't have any problem",
        "new2": "This part doesn't have any problem",
        "new3": "This part doesn't have any problem",
        "new4": "This part doesn't have any problem",
        "new5": "This part doesn't have any problem",
        "new6": "This part doesn't have any problem",
        "test": "This part doesn't have any problem",
        "data": get_object_or_404(Coin, id=user_id),
    }

    return render(request, 'coin/self.html', context=context)