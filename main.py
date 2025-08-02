import requests

import request_options

def convert_data(data, key, val):
    c_data = {}
    for d in data:
        d_key, d_val = d.get(key, ''), d.get(val, '')
        if d_key != '' and d_val != '':
            c_data[d_key] = d_val
    # return c_data

    return {d[key]: d[val] for d in data if d.get(key, '')!='' and d.get(val, '')!=''}


def get_cortar_response(cortarNo='0000000000', complexNo='3704'):
    params = {'cortarNo': f'{cortarNo}',}
    cookies = request_options.COOKIES[cortarNo]()
    headers = request_options.HEADERS[cortarNo](complexNo)

    _response = requests.get(url='https://new.land.naver.com/api/regions/list',
                             params=params,
                             cookies=cookies,
                             headers=headers)
    return _response.json()

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

def get_complex_response(complexNo):
    url = f'https://new.land.naver.com/api/articles/complex/{complexNo}?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo=123511&buildingNos=&areaNos=&type=list&order=rank'
    response = requests.get(
        url=url,
        cookies=cookies,
        headers=make_headers(complexNo),
    )
    return response.json()


if __name__ == '__main__':
    city_data = get_list_city()
    print(city_data.keys())
    cityNo = city_data.get(input('어느 시/도?'), '')
    print(cityNo)

    district_data = get_list_district(cityNo)
    print(district_data.keys())
    district_no = district_data.get(input('어느 도/구/군?'), '')
    print(district_no)

    town_data = get_list_town(district_no)
    print(town_data.keys())
    townNo = town_data.get(input('어느 읍/면/동?'), '')
    print(townNo)