from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    counter_words = 0
    for i in user_text.split(' '):
        counter_words += 1
    return render(request, 'reverse.html', {'usertext': user_text, 'usertext_reversed': user_text[::-1], 'cnt': counter_words})
