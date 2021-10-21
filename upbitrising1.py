# -*- coding: utf-8 -*-
import pyupbit
import time
import telegram

bot = telegram.Bot(token='2048593727:AAHCj630POvz-_pdx7dEYewBap7odNP7OTM')
chat_id = 139062754

access = "tmobuBWWxvYxV9B2oW8ewuv0VsRZXEj8NIApk1Qn" 
secret = "xPbZVoYxzeuDkmh9aQPJlQqxn9S6sg1edb8YnEP8" 
upbit = pyupbit.Upbit(access, secret)
print("코인 급등주 자동매매 시작")
index = 0
KRW= upbit.get_balance("KRW") # 이걸로는 되는데 def로는 왜 안됄까
tickers = pyupbit.get_tickers(fiat="KRW")

def old호가(ticker) :
    price = pyupbit.get_current_price(ticker)
    return price
      
def new호가(ticker) :
    time.sleep(30)
    price = pyupbit.get_current_price(ticker)
    return price

def old호가1(ticker) :
    time.sleep(3)
    price = pyupbit.get_current_price(ticker)
    return price
      
def new호가1(ticker) :
    time.sleep(10)
    price = pyupbit.get_current_price(ticker)
    return price

# def 거래상승(): # 거래량이 1분 전보다 1.5배인 경우
#     old거래량 =  pyupbit.get_ohlcv(ticker, interval = "minute1")
#     time.sleep(60)
#     new거래량 = pyupbit.get_ohlcv(ticker, interval = "minute1")

#     if old거래량*1.5 < new거래량:
#         lst2 # 200개의 데이터를 불러오는데 이게 맞는지?
#     return
#위의 두개를 매칭 시켜야 되는데 안되면 거래량을 빼야되려나

def 현재가(ticker):
    return pyupbit.get_current_price(ticker) # 작동 확인 / 또한, 티커에 없는 애를 넣거나 티커에 있는 애를 별도로 지정하면, 해당 녀석만 출력 됨.

def 잔고(ticker):
    return upbit.get_balance(ticker) # 종목을 지정해야만, 정보를 불러옴

def 목표가(ticker):
    return upbit.get_avg_buy_price(ticker) # 종목을 지정해야만, 정보를 불러옴

def 매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.05)
    return order # 작동확인, 티커만 "KRW-BCT" 형식으로 넣으면 작동함.

def 부분매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.1)
    return order 

def 지금매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.2)
    return order 

def 매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.05)
    return order

def 일부매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.2)
    return order

def 반매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.5)
    return order

def 풀매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker))
    return order

def 총매수금액():
    return upbit.get_amount('ALL')

# print(총매수금액())
index = 0


# while True:
#     # 데이터 스크래핑
#     url = "https://www.coingecko.com/ko/거래소/upbit"
#     resp = requests.get(url)

#     # 데이터 선택
#     bs = BeautifulSoup(resp.text,'html.parser')
#     selector = "tbody > tr > td > a"
#     columns = bs.select(selector)

#     # TOP 5 추출
#     ticker_in_krw = [x.text.strip() for x in columns if x.text.strip()[-3:] == "KRW"]
#     print(ticker_in_krw[:5])
#     time.sleep(900)

while True:
    bot.sendMessage(chat_id=chat_id, text="코인 급등주 자동 매수가 {0}분 동안 작동 중입니다.".format(index))
    index += 50
    for ticker in tickers:
        if 잔고(ticker) ==0:
            if old호가(ticker)*1.02 < new호가(ticker):
                bot.sendMessage(chat_id=chat_id, text="상승&급등주 {0}를 포착하였습니다.".format(ticker))
                if old호가1(ticker)*1.01 < new호가1(ticker):
                    지금매수(ticker)
                    bot.sendMessage(chat_id=chat_id, text="급등주 {0}를 매수하였습니다.".format(ticker))
                elif old호가1(ticker) < new호가1(ticker):
                    부분매수(ticker)
                    bot.sendMessage(chat_id=chat_id, text="상승주 {0}를 매수하였습니다.".format(ticker))
            else:
                pass
