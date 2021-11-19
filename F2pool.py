#coding:utf-8
from lxml import etree
import pygsheets
import requests
import json
import okex.Market_api as Market
import time
import Config
from bs4 import BeautifulSoup



class F2pool():
    response = ''
    def __init__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
        }
        url = 'https://www.f2pool.com/'
        self.response = requests.get(url, headers=headers).text
    ##只能小写
    def coinInfo(self,coin):
        selector = etree.HTML(self.response)
        data = selector.xpath('//*[@data-currency="'+ coin.lower() +'"]/@data-config')
        coin_dic = json.loads(data[0])

        #获取全网算力
        data = selector.xpath('//*[@data-code="'+ coin.lower() +'"]/td[3]/div/text()')
        #插入数组
        coin_dic['hashrate'] = data[0].replace('\n', '')

        return coin_dic;
