#coding:utf-8
import pygsheets

import okex.Market_api as Market
import time
import Config

api_key = Config.API_KEY
secret_key = Config.SECRET_KEY
passphrase = Config.PASSPHRASE
# flag = '1'  # 模拟盘 demo trading
flag = '0'  # 实盘 real trading

marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
#获取BTC价格
result = marketAPI.get_ticker('BTC-USDT')
btc_last_price = float(result['data'][0]["last"])

result = marketAPI.get_ticker('ETH-USDT')
eth_last_price = float(result['data'][0]["last"])

result = marketAPI.get_ticker('ZEC-USDT')
zec_last_price = float(result['data'][0]["last"])

result = marketAPI.get_ticker('DASH-USDT')
dash_last_price = float(result['data'][0]["last"])

result = marketAPI.get_ticker('DASH-USDT')
dash_last_price = float(result['data'][0]["last"])

result = marketAPI.get_ticker('DCR-USDT')
dcr_last_price = float(result['data'][0]["last"])

result = marketAPI.get_ticker('KSM-USDT')
ksm_last_price = float(result['data'][0]["last"])

#打开谷歌表格API的权限文件
client = pygsheets.authorize(service_file = "maneger.json")
# 打开谷歌表格
sh = client.open('矿机项目收益模型')
wks = sh.worksheet_by_title('常量')

# 更新价格数据
wks.update_value('F3', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

wks.update_value('B4', btc_last_price)
wks.update_value('B5', eth_last_price)
wks.update_value('B6', zec_last_price)
wks.update_value('B7', dash_last_price)
wks.update_value('B8', dcr_last_price)
wks.update_value('B9', ksm_last_price)


