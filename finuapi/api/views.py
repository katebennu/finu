from api.models import Company, Stock, ReportedEntry
from django.http import HttpResponse
import json

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


def all_companies(request):
    return HttpResponse(json.dumps({'companies': [{'ticker': c.ticker, 'name': c.name, 'industries': c.get_industries()} for c in Company.objects.all()]}))


def company_rates(request):
    c = Company.objects.get(ticker=request.GET.get('ticker'))
    year = request.GET.get('year')
    return HttpResponse(json.dumps(c.get_rates(year)))


def price(request):
    if request.method == 'GET':
        ticker = request.GET.get('ticker')
        c = Company.objects.get(ticker=ticker)
        p = Stock.objects.get(company=c).price
        return HttpResponse(json.dumps({'ticker': ticker, 'price': str(float(p))}))
    elif request.method == 'PUT':
        ticker = request.GET.get('ticker')
        p = request.GET.get('price')
        c = Company.objects.get(ticker=ticker)
        s, _ = Stock.objects.get_or_create(company=c, price=p)
        s.save()
        return HttpResponse("PUT success: " + ticker + ' ' + p)


def reported_entry(request):
    if request.method == 'GET':
        c = Company.objects.get(ticker=request.GET.get('ticker'))
        year = request.GET.get('year')
        name = request.GET.get('name')
        entry = ReportedEntry.objects.get(company=c, year=year, name=name)
        return HttpResponse('GET success: ' + c.ticker + ' ' + str(entry.value) + entry.statement)
    elif request.method == 'PUT':
        c = Company.objects.get(ticker=request.GET.get('ticker'))
        year = request.GET.get('year')
        name = request.GET.get('name')
        value = request.GET.get('value')
        statement = request.GET.get('statement')
        entry, _ = ReportedEntry.objects.get_or_create(company=c,
                                                    year=year,
                                                    name=name,
                                                    value=value,
                                                    statement=statement)
        print(entry)
        entry.save()
        return HttpResponse('GET success: ' + c.ticker + ' ' + name)
