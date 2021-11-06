import okex.Account_api as Account
import okex.Funding_api as Funding
import okex.Market_api as Market
import okex.Public_api as Public
import okex.Trade_api as Trade
import okex.subAccount_api as SubAccount
import okex.status_api as Status
import json


if __name__ == '__main__':
    api_key = ""
    secret_key = ""
    passphrase = ""
    # flag是实盘与模拟盘的切换参数 flag is the key parameter which can help you to change between demo and real trading.
    # flag = '1'  # 模拟盘 demo trading
    flag = '0'  # 实盘 real trading
    #获取持仓信息
    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
    result = accountAPI.get_positions('SWAP')
    #
    print('币种',result['data'][0]["ccy"])

    #当前价格
    ksm_last_price = float(result['data'][0]["markPx"])
    print('当前价格',ksm_last_price)
    print('开仓平均价',result['data'][0]["avgPx"])
    print('未实现收益',result['data'][0]["upl"])
    print('预估强平价',result['data'][0]["liqPx"])
    print('初始保证金',result['data'][0]["imr"])
    posSide = float(result['data'][0]["imr"]) * float(result['data'][0]["lever"])
    print('持仓量', posSide)

    #获取DCR数据
    marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
    # 获取单个产品行情信息  Get Ticker
    result = marketAPI.get_ticker('DCR-USDT')
    dcr_last_price = float(result['data'][0]["last"])
    print('DCR价格', dcr_last_price)

    #计算这个DCR的市值
    dcr_value = posSide * ksm_last_price / dcr_last_price
    print('折合DCR市值', dcr_value)
    ksm_dcr_related = (ksm_last_price/dcr_last_price)/1.94
    print('KSM/DCR相关性', ksm_dcr_related)




    tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)
    result = tradeAPI.get_orders_history('SWAP')
    # result = tradeAPI.orders_history_archive('FUTURES','KSM-USD-SWAP')

    # print(json.dumps(result))



    # print(result)