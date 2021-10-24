# -*- coding: utf-8 -*-
import pyupbit
import time
import telegram

access = "tmobuBWWxvYxV9B2oW8ewuv0VsRZXEj8NIApk1Qn" 
secret = "xPbZVoYxzeuDkmh9aQPJlQqxn9S6sg1edb8YnEP8" 
upbit = pyupbit.Upbit(access, secret)
print("코인 자동매매 시작")

# 1. *개의 코인을 거래할 수 있도록 정의 - 완료
# 2. 각 코인의 상승율, 하락율을 설정하도록 정의
# 3. 차후 대시보드를 통해 어느 코인을 거래할 것인지 지정 가능하도록,
# 4. 또한, 퍼센트도 지정 가능하도록 - 현재는 보유하지 않아야 현금의 5% 구매하나, 5% 미만시 3% 미만 상승 퍼센트에서는 5% 만큼 되도록 구매.
# 5. 백테스팅을 통해 상승장, 하락장인지를 판단하도록
# 6. 상승장일 경우, 자동으로 상승율과 하락율을 상승장에 맞게 조정
# 7. 하락장일 경우, 자동으로 상승율과 하락율을 하락장에 맞게 조정

tickers = ["KRW-DOT", "KRW-BTC", "KRW-ETH", "KRW-EOS", "KRW-DOGE"] 

KRW= upbit.get_balance("KRW") # 이걸로는 되는데 def로는 왜 안됄까

def 현재가(ticker):
    return pyupbit.get_current_price(ticker) # 작동 확인 / 또한, 티커에 없는 애를 넣거나 티커에 있는 애를 별도로 지정하면, 해당 녀석만 출력 됨.

def 잔고(ticker):
    return upbit.get_balance(ticker) # 종목을 지정해야만, 정보를 불러옴

def 목표가(ticker):
    return upbit.get_avg_buy_price(ticker) # 종목을 지정해야만, 정보를 불러옴

def 매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.05)
    return order # 작동확인, 티커만 "KRW-BCT" 형식으로 넣으면 작동함.

def 매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.05)
    return order

def 풀매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker))
    return order

def 총매수금액():
    return upbit.get_amount('ALL')
# print(총매수금액())

def 부분매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.1)
    return order 

bot = telegram.Bot(token='2048593727:AAHCj630POvz-_pdx7dEYewBap7odNP7OTM')
chat_id = 2086229730
index = 0


while True:
    for ticker in tickers:
        if 잔고(ticker) != 0 :   
                if 목표가(ticker)*0.95 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if KRW > 100000:
                        if 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.2:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20% 미만일 경우 원화 잔고의 5% 매수
                         bot.sendMessage(chat_id=chat_id, text="코인 {0} 을 물타기 중입니다.".format(ticker))
                elif 목표가(ticker)*0.9 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 10% 낮은 경우,     
                    if KRW > 100000:
                        if (총매수금액() + KRW)*0.2 < 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.35:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20~35% 일 경우 원화 잔고의 5% 매수
                         bot.sendMessage(chat_id=chat_id, text="코인 {0}의 막바지 물타기 중입니다.".format(ticker))
                elif 목표가(ticker)*1.03 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 3% 높은 가격보다 낮은 경우,  
                    if KRW > 100000:
                        if 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.05:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 5% 미만일 경우 원화 잔고의 5% 매수
                         bot.sendMessage(chat_id=chat_id, text="코인 {0}를 불타기하였습니다.".format(ticker))
                elif 목표가(ticker)*2 < 현재가(ticker):# 2. 해당종목 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                     풀매도(ticker)
                     bot.sendMessage(chat_id=chat_id, text="코인 {0} 을 전부 익절하였습니다. 익절 금액은 {1}원 입니다.".format(ticker, (현재가(ticker) - 목표가(ticker))*잔고(ticker)))
                elif 목표가(ticker)*1.05 < 현재가(ticker):# 1. 해당종목 현재 가격이 구매 가격보다 5% 높고, 보유분이 전체의 5% 이상일 경우에만 해당 코인 잔고의 5% 씩 판매 
                    if 잔고(ticker)*현재가(ticker) > (총매수금액() + KRW)*0.05: 
                     매도(ticker)  
                     bot.sendMessage(chat_id=chat_id, text="코인 {0} 을 일부 익절하였습니다. 익절 금액은 {1}원 입니다.".format(ticker, (현재가(ticker) - 목표가(ticker))*잔고(ticker)*0.05))
        else : 
            부분매수(ticker) # 1. 해당종목을 보유하지 않는 경우, 원화 잔고의 10% 매수
            time.sleep(1)
            bot.sendMessage(chat_id=chat_id, text="코인 {0}를 초기 매수하였습니다. 매수 금액은 {1}원 입니다.".format(ticker, 목표가(ticker)*잔고(ticker)))
    time.sleep(600) # 십분에 한번씩
