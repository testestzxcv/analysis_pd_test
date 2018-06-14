import json
from .api import api
import os
RESULT_DIRECTORY = '__result__/crawling'

def preprocess_tourspot_visitor(data):
    if 'csNatCnt' not in data:
        data['count_locals'] = 0
    else:
        data['count_locals'] = data['csNatCnt']
        del data['csNatCnt']

    if 'csForCnt' not in data:
        data['count_forigner'] = 0
    else:
        data['count_forigner'] = data['csForCnt']
        del data['csForCnt']

    if 'resNm' not in data:
        data['tourist_spot'] = 0
    else:
        data['tourist_spot'] = data['resNm']
        del data['resNm']

    if 'ym' not in data:
        data['date'] = 0
    else:
        data['date'] = data['ym']
        del data['ym']

    if 'sido' not in data:
        data['restrict1'] = 0
    else:
        data['restrict1'] = data['sido']
        del data['sido']

    if 'gungu' not in data:
        data['restrict2'] = 0
    else:
        data['restrict2'] = data['gungu']
        del data['gungu']

def crawling_tourspot_visitor(district, start_year, end_year):
    results = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            print('year:', year)
            print('month', month)
            datas = api.pd_fetch_tourspot_visitor(district, year = year, month = month)
            for data in datas:
                preprocess_tourspot_visitor(data)
            results += datas
    print(results)

    # save data to file
    filename = '%s/%s_tourspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)
    with open(filename, 'w', encoding='utf-8') as outfile:  # with를 쓰면 블럭 빠져나올때 자동으로 닫힌다
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)  # indent 들여쓰기 4번
        outfile.write(json_string)


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)
