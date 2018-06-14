import json
import sys
from _datetime import *
from urllib.request import Request, urlopen

def html_request(
    url='',
    encoding='utf-8',
    success=None,
    error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)
        html = resp.read().decode(encoding)

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:  # 함수가 아니면
            return html

        success(html)

    except Exception as e:
        if callable(error) is True:
            error(e)


def json_request(
    url='',
    encoding='utf-8',
    success=None,
    error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):

    try:
        request = Request(url)
        resp = urlopen(request)
        resp_body = resp.read().decode(encoding)

        json_result = json.loads(resp_body)

        print('%s : success for request[%s]' % (datetime.now(),url))

        if callable(success) is False:  # 함수가 아니면
            return json_result

        success(json_result)

    except Exception as e:
        if callable(error) is True:
            error(e)