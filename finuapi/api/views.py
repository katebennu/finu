from django.http import HttpResponse
from api.models import Company, Stock


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


def price(request):
    if request.method == 'GET':
        ticker = request.GET.get('ticker')
        c = Company.objects.get(ticker=ticker)
        stock = Stock.objects.get(ticker=c).price
        return HttpResponse('GET success: ' + ticker + ' ' + str(stock))
    elif request.method == 'PUT':
        ticker = request.GET.get('ticker')
        stock = request.GET.get('price')
        c = Company.objects.get(ticker=ticker)
        s = Stock.objects.get_or_create(ticker=c, price=stock)
        c.save()
        return HttpResponse("PUT success: " + ticker + ' ' + stock)