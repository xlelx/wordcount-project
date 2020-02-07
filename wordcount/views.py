from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    count = {}
    for word in wordlist:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'mostfreq': sorted(count.items(), key=lambda x: x[1], reverse=True)})
