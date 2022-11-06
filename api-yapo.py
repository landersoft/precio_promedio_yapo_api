import json
import requests
import pandas as pd

payload = {}
headers = {
    'x-country': 'CL',
    'x-rhsref': 'new.yapo.cl',
    'x-txref': '2fd2d2f6-9cd5-4ef0-a6bb-ffb9317da56c',
    'x-chref': 'WEB',
    'x-commerce': 'Yapo',
    'x-domain': 'Buyer',
    'x-cmref': 'client'
}
contador = 0
total = 0
listado_final = []
for i in range(10):
    
    url = 'https://public-api.yapo.cl/buyers/search?page={}&limit=47&query=%7B%22brand%22:64,%22model%22:%2243%22,' \
          '%22publisherType%22:%22private%22,%22category%22:%5B2020%5D%7D'.format(i)
    response = requests.request("GET", url, headers=headers, data=payload)
    respuesta = response.json()
    vehiculos = (respuesta.get('ads', ''))

    for v in vehiculos:
        #print(v['location'].get('regionName', ''))
        #print(v['regdate'])
        pre_url = v.get('subject', '').split(' ')
        pre_url = "-".join(pre_url)
        url = 'https://new.yapo.cl/vehiculos/'+pre_url+"_"+str(v['listId'])

        #if v['price'] > 2000000:
        #    contador += 1
        #    total = total + int(v.get('price', 0))

        listado_final.append([v['listId'], url, v.get('price', 0), v['location'].get('regionName', ''), v.get('regdate', '')])


print("promedio : {}".format(total/contador) if contador > 0 else 0)

df = pd.DataFrame(listado_final)

df.to_excel('excel.xlsx')








