from django.shortcuts import render
import random

def home(request):
    return render(request, "home.html")

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ""
    
    uppercase = request.GET.get("uppercase") is not None
    digits = request.GET.get("digits") is not None
    symbols = request.GET.get("symbols") is not None
    length = int(request.GET.get('length', 10))

    if uppercase:
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if digits:
        char.extend(list('0123456789'))
    if symbols:
        char.extend(list('!@#$%^&*~+-'))

    for i in range(length):
        password += random.choice(char)

    context = {
        'password': password,
        'uppercase': uppercase,
        'digits': digits,
        'symbols': symbols,
        'length': length
    }

    return render(request, 'home.html', context)
