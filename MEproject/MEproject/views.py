from django.shortcuts import render

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

    return render(request, 'home/index.html', context)
