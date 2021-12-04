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

tickers = ["KRW-DOT", "KRW-BTC", "KRW-ETH", "KRW-EOS"] 

bot = telegram.Bot(token='2002300988:AAHmktc9k6NGM_MS-wQKK2FiM3ys8emrB9Q')
chat_id = 2086229730
index = 0


while True:
    for ticker in tickers:
        if upbit.get_balance(ticker) != 0 :   
                if upbit.get_avg_buy_price(ticker)*0.95 > pyupbit.get_current_price(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if upbit.get_balance("KRW") > 100000:
                        if upbit.get_balance(ticker)*pyupbit.get_current_price(ticker) < (upbit.get_amount('ALL') + upbit.get_balance("KRW"))*0.2:
                         upbit.buy_market_order(ticker, upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20% 미만일 경우 원화 잔고의 5% 매수
                         bot.sendMessage(chat_id=chat_id, text="코인 {0} 을 물타기 중입니다.".format(ticker))
                elif upbit.get_avg_buy_price(ticker)*0.9 > pyupbit.get_current_price(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 10% 낮은 경우,     
                    if upbit.get_balance("KRW") > 100000:
                        if (upbit.get_amount('ALL') + upbit.get_balance("KRW"))*0.2 < upbit.get_balance(ticker)*pyupbit.get_current_price(ticker) < (upbit.get_amount('ALL') + upbit.get_balance("KRW"))*0.35:
                         upbit.buy_market_order(ticker, upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20~35% 일 경우 원화 잔고의 5% 매수
                         bot.sendMessage(chat_id=chat_id, text="코인 {0}의 막바지 물타기 중입니다.".format(ticker))
                elif upbit.get_avg_buy_price(ticker)*1.03 > pyupbit.get_current_price(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 3% 높은 가격보다 낮은 경우,  
                    if upbit.get_balance("KRW") > 100000:
                        if upbit.get_balance(ticker)*pyupbit.get_current_price(ticker) < (upbit.get_amount('ALL') + upbit.get_balance("KRW"))*0.05:
                         upbit.buy_market_order(ticker, upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 5% 미만일 경우 원화 잔고의 5% 매수
                         bot.sendMessage(chat_id=chat_id, text="코인 {0}를 불타기하였습니다.".format(ticker))
                elif upbit.get_avg_buy_price(ticker)*2 < pyupbit.get_current_price(ticker):# 2. 해당종목 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                     upbit.sell_market_order(ticker, upbit.get_balance(ticker))
                     bot.sendMessage(chat_id=chat_id, text="코인 {0} 을 전부 익절하였습니다. 익절 금액은 {1}원 입니다.".format(ticker, (pyupbit.get_current_price(ticker) - upbit.get_avg_buy_price(ticker))*upbit.get_balance(ticker)))
                elif upbit.get_avg_buy_price(ticker)*1.05 < pyupbit.get_current_price(ticker):# 1. 해당종목 현재 가격이 구매 가격보다 5% 높고, 보유분이 전체의 5% 이상일 경우에만 해당 코인 잔고의 5% 씩 판매 
                    if upbit.get_balance(ticker)*pyupbit.get_current_price(ticker) > (upbit.get_amount('ALL') + upbit.get_balance("KRW"))*0.05: 
                     upbit.sell_market_order(ticker, upbit.get_balance(ticker)*0.05)
                     bot.sendMessage(chat_id=chat_id, text="코인 {0} 을 일부 익절하였습니다. 익절 금액은 {1}원 입니다.".format(ticker, (pyupbit.get_current_price(ticker) - upbit.get_avg_buy_price(ticker))*upbit.get_balance(ticker)*0.05))
        else : 
            upbit.buy_market_order(ticker, upbit.get_balance("KRW")*0.1) # 1. 해당종목을 보유하지 않는 경우, 원화 잔고의 10% 매수
            time.sleep(1)
            bot.sendMessage(chat_id=chat_id, text="코인 {0}를 초기 매수하였습니다. 매수 금액은 {1}원 입니다.".format(ticker, upbit.get_avg_buy_price(ticker)*upbit.get_balance(ticker)))
    time.sleep(600) # 십분에 한번씩





