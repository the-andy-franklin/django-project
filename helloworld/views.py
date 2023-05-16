from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def hello_world():
    return HttpResponse("Hello, World!")

def random_quote(request):
    response = requests.get('https://api.quotable.io/quotes/random')
    if response.status_code == 200:
        quote = response.json()[0]
        content = quote['content']
        author = quote['author']
        return render(request, 'quote.html', {'quote': quote, 'content': content, 'author': author})
    else:
        return HttpResponse('Failed to fetch a random quote')    
