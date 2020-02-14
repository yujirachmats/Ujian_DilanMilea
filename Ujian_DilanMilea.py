# http://www.zipcodeapi.com/rest/{APIkeyAnda}/distance.json/{kodepos1}/{kodepos2}/km
import requests
import json


apikey = 'jFDJmg8bTHK4Cja5d3cqBv8qKAha2wia0bBDFjJAtMp774Ff3ROHgFcZJAtMokIy'
urlprovinsi = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
urlkodepos = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
url = 'http://www.zipcodeapi.com/rest/{APIkeyAnda}/distance.json/{kodepos1}/{kodepos2}/km'
dataP = requests.get(urlprovinsi)
dataK = requests.get(urlkodepos)
datamileaP = requests.get(urlprovinsi)
datamileaK = requests.get(urlkodepos)
dilanP = datadilanP.json()
dilanK = datadilanK.json()
mileaP = datamileaP.json()
mileaK = datamileaK.json()

# print(dilanP.get('BANTEN'))

kolom = list(dilanK['36'][0].keys())
dilan = 'SAMPORA'

hasil = []
for i in dilanK['36']:
    hasil.append(i['postal_code'])
    hasil.append(i['urban'])
print(hasil)

for i in dilanK['36']:
    hasil.append(i['postal_code'])
    hasil.append(i['urban'])
print(hasil)

# # print(kolom)
# out = []
# for i in dilanK['36']:


