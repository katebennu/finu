from django.http import HttpResponse
from .models import Company


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def company(request):
    if request.method == 'GET':
        ticker = request.GET.get('ticker')
        name = Company.objects.get(ticker=ticker).name
        return HttpResponse('GET success: ' + ticker + ' ' + name)
    elif request.method == 'PUT':
        ticker = request.GET.get('ticker')
        name = request.GET.get('name')
        print(ticker, name)
        c = Company(ticker=ticker, name=name)
        c.save()
        return HttpResponse("PUT success: " + ticker + ' ' + name)

