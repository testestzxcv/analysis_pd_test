import analysis_pd_test.collect.api as pdapi

# url = pdapi.pd_gen_url(
#     'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList',
#     YM='{0:04d}{1:02d}'.format(2017,1),
#     SIDO='서울특별시',
#     GUNGU='',
#     RES_NM='',
#     numOfRows=10,
#     _type='json',
#     pageNo=1
# )
#
# print(url)

for items in pdapi.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
    print(items)

