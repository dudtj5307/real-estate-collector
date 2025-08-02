import requests

import request_options

def convert_data(data, key, val):
    if type(val)==str:
        return {d[key]: d[val] for d in data if d.get(key, '')!='' and d.get(val, '')!=''}

def get_cortar_response(cortarNo='0000000000', mode='list', _params={}):
    url = f'https://new.land.naver.com/api/regions/{mode}'
    params = {'cortarNo': f'{cortarNo}',} | _params
    cookies = request_options.cookies_cortar
    headers = request_options.headers_cortar(complexNo='3704')

    return requests.get(url=url, params=params, cookies=cookies, headers=headers).json()

def get_complex_response(complexNo):
    url = f'https://new.land.naver.com/api/articles/complex/{complexNo}?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A%3AFASTSELL%3ARENTHUG&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo={complexNo}&buildingNos=&areaNos=&type=list&order=rank'
    cookies = request_options.cookies_complex
    headers = request_options.headers_cortar(complexNo=complexNo)

    return requests.get(url=url, cookies=cookies, headers=headers).json()


# request city list (시/도)
def get_list_city():
    city_data = get_cortar_response().get('regionList', [])
    return convert_data(city_data, key='cortarName', val='cortarNo')

# request district list (도/구/군)
def get_list_district(cortarNo):
    district_data = get_cortar_response(cortarNo).get('regionList', [])
    return convert_data(district_data, key='cortarName', val='cortarNo')

# request town list (읍/면/동)
def get_list_town(cortarNo):
    town_data = get_cortar_response(cortarNo).get('regionList', [])
    return convert_data(town_data, key='cortarName', val='cortarNo')

# request complex list
def get_list_complex(cortarNo):
    params = {'realEstateType':'APT:ABYG:JGC:PRE',}
    apart_data = get_cortar_response(cortarNo, mode='complexes', _params=params).get('complexList', [])
    return convert_data(apart_data, key='complexName', val='complexNo')


def get_list_products(complexNo):
    products = []
    product_data = get_complex_response(complexNo)
    articles = product_data.get('articleList', [])
    ex_keys = ['tradeTypeName', 'dealOrWarrantPrc', 'buildingName', 'floorInfo', 'direction', 'articleFeatureDesc', 'tagList']
    for article in articles:
        products.append([article.get(key,'') for key in ex_keys])

    return products

if __name__ == '__main__':

    print(get_list_products('125213'))
