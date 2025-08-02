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

    response = requests.get(url=url, params=params, cookies=cookies, headers=headers)
    return response.json()

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
def get_list_apartment(cortarNo):
    params = {'realEstateType':'APT:ABYG:JGC:PRE',}
    apart_data = get_cortar_response(cortarNo, mode='complexes', _params=params).get('complexList', [])
    print(apart_data)
    return convert_data(apart_data, key='complexName', val='complexNo')


def get_list_products(complexNo):
    pass


if __name__ == '__main__':
    # city_data = get_list_city()
    # print(city_data.keys())
    # cityNo = city_data.get(input('어느 시/도?'), '')
    # print(cityNo)
    #
    # district_data = get_list_district(cityNo)
    # print(district_data.keys())
    # district_no = district_data.get(input('어느 도/구/군?'), '')
    # print(district_no)
    #
    # town_data = get_list_town(district_no)
    # print(town_data.keys())
    # townNo = town_data.get(input('어느 읍/면/동?'), '')
    # print(townNo)

    print(get_list_apartment('1174010200'))

    pass