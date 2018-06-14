from datetime import datetime
from urllib.parse import urlencode
from .web_request import json_request

SERVICE_KEY = '6m9Oq%2F9j8cIEp6w%2F3PmNrbAS1P17y24uk3Q2xloOH0WyDrSXbGHGpnF3Pf%2Bob8J6AW2k2HO%2BygzGcjrnyKNgog%3D%3D'

def pd_gen_url(endpoint, **param):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(param), SERVICE_KEY)
    return url


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):
    print('year', year)
    print('month', month)
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    url = pd_gen_url(
        endpoint,
        YM='{0:04d}{1:02d}'.format(year,month),
        SIDO= district1,
        GUNGU='',
        RES_NM='',
        numOfRows=10,
        _type='json',
        pageNo=1
    )

    json_result = json_request(url=url)

    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None

