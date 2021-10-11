# -*- coding: utf-8 -*-
import pyupbit
import time
import requests

access = "tmobuBWWxvYxV9B2oW8ewuv0VsRZXEj8NIApk1Qn" 
secret = "xPbZVoYxzeuDkmh9aQPJlQqxn9S6sg1edb8YnEP8" 
upbit = pyupbit.Upbit(access, secret)
token = "xoxb-2589539244755-2574957952327-wmrjDcfOqqDTspFUnSEewf90"
channel = "#upbitauto"
text = "코인 자동매매가 작동중입니다."

print("코인 자동매매 시작")
tickers = ["KRW-BTC", "KRW-DOT", "KRW-ETC", "KRW-ETH", "KRW-DOGE"]
KRW= upbit.get_balance("KRW")
def 현재가(ticker):
    return pyupbit.get_current_price(ticker)
def 잔고(ticker):
    return upbit.get_balance(ticker)
def 목표가(ticker):
    return upbit.get_avg_buy_price(ticker)
def 매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.05)
    return order 
def 매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.05)
    return order
def 풀매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker))
    return order
def 총매수금액():
    return upbit.get_amount('ALL')
while True:
    for ticker in tickers:
        if 잔고(ticker) > 0.000000001 :   
                if 목표가(ticker)*0.95 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if KRW > 100000:
                        if 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.2:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20% 미만일 경우 원화 잔고의 5% 매수
                elif 목표가(ticker)*0.9 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 10% 낮은 경우,     
                    if KRW > 100000:
                        if (총매수금액() + KRW)*0.2 < 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.35:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20~35% 일 경우 원화 잔고의 5% 매수
                elif 목표가(ticker)*1.03 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 3% 높은 가격보다 낮은 경우,  
                    if KRW > 100000:
                        if 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.05:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 5% 미만일 경우 원화 잔고의 5% 매수
                elif 목표가(ticker)*2 < 현재가(ticker):# 2. 해당종목 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                     풀매도(ticker)    
                elif 목표가(ticker)*1.05 < 현재가(ticker):# 1. 해당종목 현재 가격이 구매 가격보다 5% 높고, 보유분이 전체의 5% 이상일 경우에만 해당 코인 잔고의 5% 씩 판매 
                    if 잔고(ticker)*현재가(ticker) > (총매수금액() + KRW)*0.05: 
                     매도(ticker)  
        else : 
            매수(ticker) # 1. 해당종목을 보유하지 않는 경우, 원화 잔고의 5% 매수
        time.sleep(60) # 위의 명령은 매 1분마다 적용
    requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text})
    time.sleep(600) 
