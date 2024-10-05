from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gems_index(request):
    return render(request, 'gems/index.html', {
        'gems':gems
    })

gems = [
    {'name': 'Garren Park'},
    {'name': 'Hayward Regional Park'},
    {'name': 'Coyote Hills'}
]