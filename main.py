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
    product_data = get_complex_response(complexNo)
    print(product_data.json())

if __name__ == '__main__':

    print(get_list_complex('125213'))

    cookies = {
        'NNB': '7QZASPCQWY2GO',
        'NAC': 'XTILBYwYWaTy',
        'nid_inf': '1730481252',
        'NID_AUT': 'DE1NRGb53R7UvsjI/RorvrpWPiFql0Z+52qbzbN4T1+Fvrzb78ZovAXjmivNpeWb',
        'nhn.realestate.article.rlet_type_cd': 'A01',
        'nhn.realestate.article.trade_type_cd': '""',
        'nhn.realestate.article.ipaddress_city': '4100000000',
        '_fwb': '175CX3OZdfiEwuu8EniCZBL.1754098387335',
        'NACT': '1',
        'landHomeFlashUseYn': 'Y',
        '_fwb': '175CX3OZdfiEwuu8EniCZBL.1754098387335',
        'NID_SES': 'AAABfxAP4hkm8Df24pKm6EdkJ0Hmmi5YiEoxzVv9UZsHT54mYfIPhMboJ5H7RyvptUIoVZxHzyVEnBBW12dNU/DO8qpVhxzSXYfxQqAtn1av4nJrPW+hjqMLm2S+B2bF5SxF1gbVcLMg+8DVi9yFOXuR7lB/DhJXImD/CqcboXR46J5HKxLfJZ+9xgk40Mx4YeoyZJGfoBc3ZVUPvdZoClFY7DfIAIcC2IvIqfMA76CsK7zKswZgqQwU3nz7ZFUxliShRAbrrLAIogJRDeRdMKsCdV8uqXZACbkPaJhS/EhDnbecVrTXPP7yDwgHKlSE6LJhmuvNtR9WkPMfaIxNa39lizgRVqG8lDJ/FQbxWYKhf7ef3pJ6mHHHOOiHDsZIbCvcZyBQ8ulj1OEmEefWwQACZgcDgxevSH7jZHu7h4vnXQE8YfrS9I8VDbRPFVEAYI4kvRRHfbacgg7LDfIQAOMwU6qnfa5rK/dTmDwvd7Pc+/d4cj3fuIMuFY2R7mf+Sfz2uQ==',
        'SRT30': '1754158543',
        'REALESTATE': 'Sun%20Aug%2003%202025%2003%3A30%3A19%20GMT%2B0900%20(Korean%20Standard%20Time)',
        'PROP_TEST_KEY': '1754159419409.b18b534a66dfed0922a71ab3d204fe2f8f602e710823e1d69dbc7f297ae770ae',
        'PROP_TEST_ID': '13d2b936b27b5b96bad36c946f0eae5bdd0ea26bc56668b4f7531c3ddc698842',
        'SRT5': '1754161380',
        'BUC': '0u5YniYCU8IW93K3AesiBOwSlzkS94CNeGBO05wRY2E=',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NTQxMDEyNTMsImV4cCI6MTc1NDExMjA1M30.rjOwhw2sPnJ4sJSQoWseeOnHSDDB74C-CF5Ja-FPL1A',
        'priority': 'u=1, i',
        'referer': 'https://new.land.naver.com/complexes/3634234ssdfsddfsf936?ms=37.3014924,127.0805943,17&a=APT:ABYG:JGC:PRE&e=RETAIL&y=FASTSELL:RENTHUG',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://new.land.naver.com/api/articles/complex/125213?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A%3AFASTSELL%3ARENTHUG&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo=125213&buildingNos=&areaNos=&type=list&order=rank',
        cookies=cookies,
        headers=headers,
    )

    print(response.json())