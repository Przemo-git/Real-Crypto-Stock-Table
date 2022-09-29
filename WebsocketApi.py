import websocket,json,random


ws=websocket.WebSocket()

ws.connect('ws://localhost:8000/ws/tableData/')

import requests


i=0
while i <= 21:

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=21&page=1&sparkline=false'
    data = requests.get(url).json()
    data1 = data[0]['id']
    data2 = data[1]['id']
    data3 = data[2]['id']
    data4 = data[3]['id']
    data5 = data[20]['id']
    print(data1, data2)
    listOfindex=['data1','data2','data3','data4','data5']
    price1 = data[0]['current_price']
    price2 = data[1]['current_price']
    price3 = data[2]['current_price']
    price4 = data[3]['current_price']
    price5 = data[20]['current_price']
    y = [price1, price2, price3, price4, price5]
    marketCap1 = data[0]['market_cap']
    marketCap2 = data[1]['market_cap']
    marketCap3 = data[2]['market_cap']
    marketCap4 = data[3]['market_cap']
    marketCap5 = data[20]['market_cap']
    z = [marketCap1, marketCap2, marketCap3, marketCap4, marketCap5]
    volume1 = data[0]['total_volume']
    volume2 = data[1]['total_volume']
    volume3 = data[2]['total_volume']
    volume4 = data[3]['total_volume']
    volume5 = data[20]['total_volume']
    a = [volume1, volume2, volume3, volume4, volume5]

    for i in range(len(data)):
        print(i)
        import time
        time.sleep(2)
        x = listOfindex
        try:
            # x = listOfindex
            pp=json.dumps({'indexName':x[i],'value':y[i],'marketvalue':z[i],'volumevalue':a[i]})
            print (pp)
            ws.send(pp)
        except IndexError:
            continue

