from django.http import HttpResponse
import requests

def hello_world(request):
    return HttpResponse("Hello, World!")

def random_quote(request):
    response = requests.get('https://api.quotable.io/quotes/random')
    if response.status_code == 200:
        quote = response.json()
        print(quote)
        return HttpResponse(quote)
    else:
        return HttpResponse('Failed to fetch a random quote')    
