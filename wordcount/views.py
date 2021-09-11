from operator import itemgetter
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split( )
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sort = sorted(worddictionary.items(), key=itemgetter(1),reverse=True)
    return render(request,'count.html',{'count':len(wordlist),'worddictionary':sort,'fulltext':fulltext})
def about(request):
    return render(request,'about.html')
