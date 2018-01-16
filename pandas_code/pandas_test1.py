import numpy as np
import pandas as pd
import requests
import json
#import urllib
from urllib import request, parse

url = 'https://www.lfd.uci.edu/~gohlke/pythonlibs/'
url2 = url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'

#resp = request.urlopen(url)

headers = {
      'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
      'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
      'Connection': 'keep-alive'
}

req = request.Request(url, headers=headers)
page = request.urlopen(req).read()
page = page.decode('utf-8')
url22 = request.geturl()
print(url22)
#print(page)
