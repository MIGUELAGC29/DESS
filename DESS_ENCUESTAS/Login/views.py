from django.shortcuts import render


def peticionCurp(request):
    return render(request, 'pedirCurp.html')