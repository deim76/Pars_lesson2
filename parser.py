
import requests

url = 'https://5ka.ru/'
url_products='api/v2/special_offers/'
url_categories='/api/v2/categories'

header = ''


def get_data(url, list: list):
    request_url = requests.get(url)
    list.append(request_url.json())
    return list
def get_products():
    catalogs = get_data(url + url_categories, [])
    products = []
    index=0
    for i in catalogs[0]:
        request_url = requests.get(
            url + url_products + '?categories=' + i['parent_group_code'] + '&records_per_page=20')
        if request_url.status_code==504:
           continue
        data = request_url.json()
        for item in data['results']:
            dict_pr = dict()
            dict_pr['Catalog_code'] = index
            dict_pr['name'] = (item['name'])
            dict_pr['plu'] = (item['plu'])
            dict_pr['Price'] = (item['current_prices']['price_promo__min'])
            products.append(dict_pr)

        # while request_url.next:
        #          request_url = requests.get(request_url.next)
        #          data = request_url.json()
        #          for item in data['results']:
        #                dict_pr = dict()
        #             dict_pr['Catalog_code'] = index
        #             dict_pr['name'] = (item['name'])
        #             dict_pr['plu'] = (item['plu'])
        #             dict_pr['Price'] = (item['current_prices']['price_promo__min'])
        #             products.append(dict_pr)
        index+=1
    return products


class Parser:

    def __init__(self):
       self.catalogs = get_data(url + url_categories, [])
       self.products = get_products()


