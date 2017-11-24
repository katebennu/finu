# first try export
import requests

QUERY_TEMPLATE = 'https://www.google.fi/search?q={}'


def query(a, b):
    return len(
        requests.get(QUERY_TEMPLATE.format(str(a)+'%2B'+str(b))).text
    )


def first_fun(a, b):
    return a + b + query(a, b)

