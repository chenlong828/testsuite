#!/usr/bin/env python
# coding:utf-8
import _env
import requests
import json
from misc import config
from jsdict import JsDict

class restapi(object):
    _link = None
    _data = ()
    _headers = ()

    @classmethod
    def get(cls, url, headers={}, data={}):
        return cls._request(url, headers, data, requests.get)

    @classmethod
    def post(cls, url, headers={}, data={}):
        return cls._request(url, headers, data, requests.post)

    @classmethod
    def _request(cls, url, headers, data, method):
        result = method(
            '%s%s' % (config.API_HOST, url),
            headers=headers,
            data=data
        ).content
        try:
            r = json.loads(result)
            return r
        except ValueError:
            print result
            raise
            


def wrapper(_url):
    def _(headers={}, body={}, method='post', url=''):
        #return url, headers, body, method 
        do = restapi.post
        if method == 'get':
            do = restapi.get
        request_url = url if url else _url
        return do(
            request_url,
            data = body,
            headers = headers
        )
    return _