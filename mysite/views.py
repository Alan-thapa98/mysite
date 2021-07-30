# i create the for the viwes of th eusers in the website.
from django.http import HttpResponse
from django.shortcuts import render
# char = charater okay!


def index(request):
    # params = {'name': 'Alan', 'palce': 'Nepal'}
    return render(request, 'index.html')


# def index(request):
#     # params = {'name': 'Alan', 'palce': 'Nepal'}
#     return render(request, 'shop/index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcapatilizer = request.POST.get('fullcapatilizer', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcapatilizer == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not(djtext[index] == " "):
                    analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'
        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcapatilizer != "on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')


def capitalizer(request):
    return HttpResponse("<h1> capitalizer the django programming framework. </h1>")


def newlineremove(request):
    return HttpResponse("<h1> newlineremove the django programming framework. </h1>")


def spaceremove(request):
    return HttpResponse("<h1> spaceremove the django programming framework. </h1>")


def charcount(request):
    return HttpResponse("<h1> charcount the django programming framework. </h1>")

# exercise one


def exe1(request):
    return HttpResponse(''' <h1><a href='one'>claick one</a></h1>''')


def contactus(request):
    # params = {'name': 'Alan', 'palce': 'Nepal'}
    return render(request, 'contactus.html')


def about(request):
    # params = {'name': 'Alan', 'palce': 'Nepal'}
    return render(request, 'about.html')
