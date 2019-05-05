from django.http import HttpResponse
from django.shortcuts import render
import operator

def home (request):
    return render (request,'home.html')

def count (request):
    wordList = request.GET['fullText'].split()
    dict = {}

    for word in wordList :
        if (word not in dict):
            dict[word] = 1
        else :
            dict[word]+=1
    sortedArr = sorted(dict.items(),key = operator.itemgetter(1), reverse = True)
    return render (request,'count.html', {'sortedArr' : sortedArr, 'count' : len(wordList)})

def about (request):
    return render (request , 'about.html')
