import pyupbit
import time

access = "tmobuBWWxvYxV9B2oW8ewuv0VsRZXEj8NIApk1Qn" 
secret = "xPbZVoYxzeuDkmh9aQPJlQqxn9S6sg1edb8YnEP8" 
upbit = pyupbit.Upbit(access, secret)

# 자동매매 

# def get_target_price(ticker, k):
#     """변동성 돌파 전략으로 매수 목표가 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
#     target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
#     return target_price

# class RealOrder(pyupbit.Upbit):
#     def __init__(self, key0, key1):
#         super().__init__(key0, key1)

#     def get_current_price(self, ticker):
#         while True:
#             price = pyupbit.get_current_price(ticker)
#             if price != None:
#                 return price
#             else:
#                 print("get_current_price wait")
#                 time.sleep(1800)

#     def buy_market_order(self, ticker, cash):
#         while True:
#             order = super().buy_market_order(ticker, cash)
#             if order == None or 'error' in order:
#                 print("buy_market_order wait", ticker, cash, order)
#                 time.sleep(1800)
#                 continue
#             else:
#                 return order

#     def get_order_detail(self, uuid):
#         while True:
#             order = super().get_order(uuid)
#             if order != None and len(order['trades']) > 0:
#                 return order
#             else:
#                 print("get_order_detail wait", uuid)
#                 time.sleep(1800)

#     def get_outstanding_order(self, ticker):
#         while True:
#             order = super().get_order(ticker)
#             if order != None and len(order) == 0:
#                 return order
#             else:
#                 print("get_outstanding_order wait", ticker)
#                 time.sleep(1800)

#     def get_balance(self, ticker="KRW"):
#         while True:
#             volume = super().get_balance(ticker)
#             if volume != None:
#                 return volume
#             else:
#                 print("get_balance wait", ticker)
#                 time.sleep(1800)

#     def sell_market_order(self, ticker, volume):
#         while True:
#             order = super().sell_market_order(ticker, volume)
#             if order != None and "uuid" in order:
#                 return order
#             else:
#                 print(volume, order)
#                 print("sell_market_order wait", volume, order)
#                 time.sleep(1800)


# def ETH_target_price() :
#     ETH_target_price = upbit.get_avg_buy_price("KRW-ETH")
#     return ETH_target_price


# def ETH_current_price() :
#     ETH_current_price = pyupbit.get_current_price("KRW-ETH") 
#     return ETH_current_price


while True:
        if upbit.get_balance("KRW-ETC") > 0.0000000000001 :   
                if upbit.get_avg_buy_price("KRW-ETC")*0.95 > pyupbit.get_current_price("KRW-ETC"): # 2. 이더리움 클래식을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if upbit.get_balance("KRW") > 100000:
                        upbit.buy_market_order("KRW-ETC", upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상인 경우 잔고의 5% 매수
                    elif upbit.get_balance("KRW") > 50000:
                        upbit.buy_market_order("KRW-ETC", upbit.get_balance("KRW")*0.1)# 2-2. 잔고가 5만원 이상인 경우 잔고의 10% 매수
                    elif upbit.get_balance("KRW") > 20000:
                        upbit.buy_market_order("KRW-ETC", upbit.get_balance("KRW")*0.3)# 2-3. 잔고가 2만원 이상인 경우 잔고의 30% 매수
                    elif upbit.get_balance("KRW") > 10000:
                        upbit.buy_market_order("KRW-ETC", upbit.get_balance("KRW")*0.9)# 2-4. 잔고가 만원 이상인 경우 잔고의 90% 매수
  
                elif upbit.get_avg_buy_price("KRW-ETC")*2 < pyupbit.get_current_price("KRW-ETC"):# 2. 이더리움 클래식 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                 upbit.sell_market_order("KRW-ETC",upbit.get_balance("KRW-ETC"))   
    
                elif upbit.get_avg_buy_price("KRW-ETC")*1.05 < pyupbit.get_current_price("KRW-ETC"):# 1. 이더리움 클래식 현재 가격이 구매 가격보다 5% 높고, 
                    if upbit.get_balance("KRW-ETC")*pyupbit.get_current_price("KRW-ETC") > (upbit.get_balance("KRW-ETH")*pyupbit.get_current_price("KRW-ETH") + upbit.get_balance("KRW-ETC")*pyupbit.get_current_price("KRW-ETC") + upbit.get_balance("KRW-BTC")*pyupbit.get_current_price("KRW-BTC") + upbit.get_balance("KRW-DOT")*pyupbit.get_current_price("KRW-DOT") + upbit.get_balance("KRW-DOGE")*pyupbit.get_current_price("KRW-DOGE") + upbit.get_balance("KRW"))*0.05: # 보유금액이 총 금액의5%보다 높은 경우, 보유분의 5% 매도
                     upbit.sell_market_order("KRW-ETC", upbit.get_balance("KRW-ETC")*0.05)  
        else : 
                upbit.buy_market_order("KRW-ETC", upbit.get_balance("KRW")*0.05) # 1. 이더리움 클래식을 보유하지 않는 경우, 잔고의 5% 매수
        time.sleep(600) # 위의 명령은 매 반시간마다 적용

#작동됨.
