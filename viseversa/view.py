from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    return render(request, 'reverse.html', {'usertext': user_text[::-1]})
