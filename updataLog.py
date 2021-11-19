#coding:utf-8
import pygsheets
import time
import F2pool


def unix_time(dt):
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp



#打开谷歌表格API的权限文件
client = pygsheets.authorize(service_file = "maneger.json")
# 打开谷歌表格
sh = client.open('矿机项目收益模型')
wks = sh.worksheet_by_title('历史记录')

# 获取最后更新的时间戳
wks.update_value('F3', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
last_time = wks.cell('B3')
last_time_int = unix_time(last_time.value)
#获取时间间隔
distance_time = wks.cell('B2')
now_time = time.time()

#判断是否需要到了更新的时间
if now_time - last_time_int < int(distance_time.value):
    print('end')
    exit()

#获取最后更新的行数
last_data = wks.cell('B4')
last_data_num = last_data.value
last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


#获取f2pool信息
f2pool = F2pool.F2pool()
#获取BTC信息
btc_info = f2pool.coinInfo('BTC')
#更新BTC信息
wks.update_value('C' + last_data_num, btc_info['hashrate'])
wks.update_value('D' + last_data_num, btc_info['estimatedProfit'])
wks.update_value('E' + last_data_num, btc_info['price'])
wks.update_value('F' + last_data_num, btc_info['difficulty'])
wks.update_value('G' + last_data_num, last_time)

#获取ETH信息
eth_info = f2pool.coinInfo('ETH')
#更新BTC信息
wks.update_value('H' + last_data_num, eth_info['hashrate'])
wks.update_value('I' + last_data_num, eth_info['estimatedProfit'])
wks.update_value('J' + last_data_num, eth_info['price'])
wks.update_value('K' + last_data_num, eth_info['difficulty'])
wks.update_value('L' + last_data_num, last_time)

dash_info = f2pool.coinInfo('DASH')
#更新BTC信息
wks.update_value('M' + last_data_num, dash_info['hashrate'])
wks.update_value('N' + last_data_num, dash_info['estimatedProfit'])
wks.update_value('O' + last_data_num, dash_info['price'])
wks.update_value('P' + last_data_num, dash_info['difficulty'])
wks.update_value('Q' + last_data_num, last_time)

#获取dash信息
dcr_info = f2pool.coinInfo('DCR')
#更新BTC信息
wks.update_value('R' + last_data_num, dcr_info['hashrate'])
wks.update_value('S' + last_data_num, dcr_info['estimatedProfit'])
wks.update_value('T' + last_data_num, dcr_info['price'])
wks.update_value('U' + last_data_num, dcr_info['difficulty'])
wks.update_value('V' + last_data_num, last_time)




#更新时间
wks.update_value('B3', last_time)
wks.update_value('B4', int(last_data_num) + 1)












