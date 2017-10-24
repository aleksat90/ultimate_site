from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup
import re

# Create your views here.


def chartView(request):
	print('chart View pokrenut')
	print('pokrenut view')
	gradovi = ['cacak','beograd','smederevo','zlatibor','kopaonik','nis','kraljevo','novi-sad','subotica']
	temp=[]
	for i in range(len(gradovi)):
		tre_temp = citanjeTemperature(gradovi[i])
		temp.append(tre_temp)
		print(gradovi[i]+" "+tre_temp)

	print('Citanje zavrseno')
	return render(request, 'charts/chart.html', {'cacak': temp[0],
													'beograd': temp[1],
													'smederevo': temp[2],
													'zlatibor': temp[3],
													'kopaonik': temp[4],
													'nis': temp[5],
													'kraljevo': temp[6],
													'novisad': temp[7],
													'subotica':temp[8]})


def citanjeTemperature(grad):
	quote_page = 'https://www.weather2umbrella.com/weather-forecast-'+grad+'-serbia-en/current'
	page = urllib.request.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	temp = soup.find('div', attrs={'class': 'current_temperature_data hidden-xs'}).text
	temp=re.findall(r'\d+',temp)
	return temp[0]


# Take out the <div> of name and get its value
