from django.shortcuts import render
import requests

def getik(request):

    response = requests.get("https://www.cbr-xml-daily.ru/latest.js").json()
    currencies = response.get('rates')

    if request.method == 'GET':

        context = {
          'currencies': currencies
        }

        return render(request=request, template_name='myapp/index.html', context=context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request=request, template_name='myapp/index.html', context=context)