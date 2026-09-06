from django.shortcuts import render

def index(request):

    new1 = "This part doesn't have any problem"
    new2 = "This part doesn't have any problem"
    new3 = "This part doesn't have any problem"
    new4 = "This part doesn't have any problem"
    new5 = "This part doesn't have any problem"
    new6 = "This part doesn't have any problem"
    test = "This part doesn't have any problem"
        

    context = { "new1" : new1 , "new2" : new2 , "new3" : new3 , "new4" : new4 , "new5" : new5 , "new6" : new6 , "test" : test }
    return render(request, 'coin/index.html', context=context)