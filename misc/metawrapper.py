#!/usr/bin/env python
#coding:utf-8
import _env
from string_tool import cap_split
from vps_api import wrapper

def get_url_builder(base_name):
    base_name = base_name[1:]

    def product(self, name):
        li = cap_split(name)
        url = '/product/%s/%s' % (li[-1].lower(), name)
        return url

    sales = lambda self, x: '/sales/admin/%s' % x
    account = order = bestpay = billing = lambda self, x: '/%s/%s' % (base_name.lower(), x)
    iam_user = lambda self, x: '/iam/user/%s' % x

    return locals()[base_name.lower()]

def _get_attr(self, name):
    url = self.build_url(name)
    return wrapper(url)

class _Model(type):
    def __new__(cls, name, bases, attrs):
        new_class = type.__new__(cls, name, bases, attrs)
        new_class.build_url = get_url_builder(name)
        new_class.__getattr__ = _get_attr
        new_class.__doc__ = '''
p = Product()
p.CreateCatalog(headers={}, body={}, method='post')
'''
        return new_class