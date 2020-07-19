# I had created that file


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')  # taking text

    removepunc = request.POST.get('removepunc','off')
    charcount = request.POST.get('charcount','off')
    capitalise = request.POST.get('capitalise','off')

    analyzed = ""

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        purpose = "Removed punctuations"
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        text=analyzed

    if charcount == "on":
        count=0
        for char in text:
            count+=1
        analyzed="There are total {} characters.".format(count)+"\n\n\n"+text

    if capitalise == "on":
        analyzed=""
        for char in text:
            analyzed += char.upper()
        print(analyzed)
    params={'purpose':'Task performed','analyzed_text':analyzed}
    return render(request,'analyze.html',params)

