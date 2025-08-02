from collections import defaultdict

cookies_cortar = {
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
        'REALESTATE': 'Sat%20Aug%2002%202025%2011%3A20%3A53%20GMT%2B0900%20(Korean%20Standard%20Time)',
        'PROP_TEST_KEY': '1754101253881.0ecc779a4e49575223a349848209282993046df5ff3caa22ea16ff56e7bde5c2',
        'PROP_TEST_ID': '1197261c7a7fabdaf960c75be9a5d328b5969f20b877b0c4efed6a7cec638181',
        'SRT30': '1754122385',
        'NID_SES': 'AAABh66HYkbRQDg1PTLCY+FClLAW0U3in6di1Bl+3Ff50oMTatvECDIH5EwNwTNDZusloWo4waegBzsUJzQ2gnbFsjN14uJNVp04oKt0ML1T+TFqDWzX1Ae1icC3FWKolrlOhxtJE+3OCOZtrm00PDKUgNW7HI2nL4GiDQJvbbYKc1h7KNJOHDgUJ5QSNnSGry/yuyHH7vb4xxcwpA5caxvYyVbJUDJiFg6qMH6vNHmXSDnlpdI8h0gcVwhu/ACJrwpKXxsM+v24OWYIeVnMHrkmsHcjOOTw0e38Hq+0GvPphatZFPrKUnGKsTxzdTqudMAuXDrk0UJnQvSzxUgXiN9vG7CkJuxMlHhBIt0JcnPusQh7kqZAUF81Pa6fxWye3xxOVQabAbFZWiHFBQcmIUyOqGlkVMsuCkTqGhmdGfTJfdJ9m3slSkuZfiCIv1pZ8nqtkUaak1zy8RrmYwcCA+Bfn2+hwUqDj05g7PtItg1V8v5iTaHkkfW4mSs/AJvhCvP99vldNMTCCu6X2Qz8/V2Vm6I=',
        'BUC': '5RtqaIXo1q2wljbIW2koinNz3gQ9Uk7dUsj5YeoscTQ=',
}

cookies_complex = {
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

def headers_cortar(complexNo='3704'):
    _headers = {
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NTQxMDEyNTMsImV4cCI6MTc1NDExMjA1M30.rjOwhw2sPnJ4sJSQoWseeOnHSDDB74C-CF5Ja-FPL1A',
        'priority': 'u=1, i',
        'referer': f'https://new.land.naver.com/complexes/{complexNo}?ms=37.30345,127.07615,16&a=APT:ABYG:JGC:PRE&e=RETAIL&y=FASTSELL:RENTHUG',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }
    return _headers

if __name__ == '__main__':
    for key in _headers.keys():
        if _headers[key] != headers_complex[key]:
            print(key)
            print(_headers[key])
            print(headers_complex[key])
    pass