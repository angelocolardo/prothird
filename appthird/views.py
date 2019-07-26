from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = { 'insert_me': "Help me! from appthird/help.html"}
    return render(request, 'appthird/help.html', context=my_dict)