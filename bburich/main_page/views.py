from django.shortcuts import render

def index(request):
    template = 'main_app/index.html'
    return render(request, template)