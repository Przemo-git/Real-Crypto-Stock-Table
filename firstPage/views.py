from django.shortcuts import render
import requests
from django.http import HttpResponse


# Create your views here.


# #1
# def index(request):
#     return render(request, 'index.html', {
#         'a':'a'
#     })


#na końcu buduj dane + tabela i javascript
# def index(request):
#     #Wpisuję dane początkowe, listOfindex from ipynb
#     data = {'stock1': {'name': 'Stock1', 'opening': 45346, 'volume': 1234, 'price': 1},
#             'stock2': {'name': 'Stock2', 'opening': 1889, 'volume': 234235, 'price': 1},
#             'stock3': {'name': 'Stock3', 'opening': 1883, 'volume': 5346, 'price': 1},
#             'stock4': {'name': 'Stock4', 'opening': 1884, 'volume': 56457, 'price': 1},
#             'stock5': {'name': 'Stock5', 'opening': 1881, 'volume': 56457, 'price': 1},
#
#             }
#     context = {'data': data, 'tableheader': ['name', 'opening', 'volume', 'price']}
#     return render(request, 'index.html', context)



# def index(request):
#     #url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
#     url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
#     data = requests.get(url).json()
#
#     #return HttpResponse(data)
#     context = {'data':data}
#     print(data)
#     return render(request, 'main.html', context)


def index(request):
    #Wpisuję dane początkowe, listOfindex from ipynb
    data = {'data1': {'name': 'Bitcoin', 'marketcap': 1, 'volume': 1234, 'price': 1},
            'data2': {'name': 'Etherum', 'marketcap': 1, 'volume': 234235, 'price': 1},
            'data3': {'name': 'Tether', 'marketcap': 1, 'volume': 234235, 'price': 1},
            'data4': {'name': 'Usd-coin', 'marketcap': 1, 'volume': 234235, 'price': 1},
            'data5': {'name': 'Litecoin', 'marketcap': 1, 'volume': 234235, 'price': 1},
            }
    context = {'data': data, 'tableheader': ['name', 'marketcap', 'volume', 'price']}
    return render(request, 'index.html', context)





