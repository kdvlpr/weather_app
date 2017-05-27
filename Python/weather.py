import requests
from bs4 import *

def weather():

    try:

        country = str(input('Enter your country name : '))

        city = str(input('Enter your city name : '))

        search_algorithm = ('https://www.timeanddate.com/weather/'+country+'/'+city)

        response = requests.get(search_algorithm)

        html = response.text
        html_bs = BeautifulSoup(html,"html.parser")

        parse = (html_bs.body.find('tr', attrs={'class': 'h2 soft'}).text)

        split = parse.split()
        parse_split = (split[0])

        print('\n')
        print(city + " Temperature is " + str(parse_split) + " Centigrade.")

    except AttributeError:
        print("Sorry, we found no match for this location.")

weather()

wait = input()
