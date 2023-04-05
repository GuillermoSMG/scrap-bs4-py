import requests
from bs4 import BeautifulSoup

url = 'https://listado.mercadolibre.com.uy/inmuebles/apartamentos/alquiler/maldonado/maldonado/_PriceRange_0UYU-25000UYU'
response = requests.get(url)

html_text = response.text
soup = BeautifulSoup(html_text, 'lxml')

houses = soup.find_all(
    'li', class_="ui-search-layout__item")

for house in houses:
    house_price = house.find(
        'span', class_="price-tag-text-sr-only").text

    house_desc = house.find(
        'h2', class_="ui-search-item__title shops__item-title").text

    house_url = house.find(
        'a', class_="ui-search-link").get('href')

    house_ubication = house.find(
        'span', class_="ui-search-item__group__element ui-search-item__location shops__items-group-details").text

    print(f'''
    Descripcion: {house_desc}
    Precio: {house_price}
    URL: {house_url}
    Ubicacion: {house_ubication}
    ''')
