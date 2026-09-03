from django.shortcuts import render

def index(request):




    coin={
        'coin': None
    } 
    return render(request, 'coin/index.html', context=coin)
