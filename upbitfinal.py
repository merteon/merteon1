# -*- coding: utf-8 -*-
import time
from upbitclass import *


while True:
    for ticker in tickers:
        if 잔고(ticker) > 0.000000001 :   
                if 목표가(ticker)*0.95 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                        if 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.2:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20% 미만일 경우 원화 잔고의 5% 매수

                elif 목표가(ticker)*0.9 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 10% 낮은 경우,     
                        if (총매수금액() + KRW)*0.2 < 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.35:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 20~35% 일 경우 원화 잔고의 5% 매수

                elif 목표가(ticker)*1.03 > 현재가(ticker): # 2. 해당종목을 보유면서, 현재 가격이 구매 가격보다 3% 높은 가격보다 낮은 경우,  
                        if 잔고(ticker)*현재가(ticker) < (총매수금액() + KRW)*0.05:
                         매수(ticker)# 2-1. 잔고가 10만원 이상이면서 보유분이 전체의 5% 미만일 경우 원화 잔고의 5% 매수

                elif 목표가(ticker)*2 < 현재가(ticker):# 2. 해당종목 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                     풀매도(ticker)
    
                elif 목표가(ticker)*1.05 < 현재가(ticker):# 1. 해당종목 현재 가격이 구매 가격보다 5% 높고, 보유분이 전체의 5% 이상일 경우에만 해당 코인 잔고의 5% 씩 판매 
                    if 잔고(ticker)*현재가(ticker) > (총매수금액() + KRW)*0.05: 
                     매도(ticker)  
        else : 
            매수(ticker) # 1. 해당종목을 보유하지 않는 경우, 원화 잔고의 5% 매수
    bot.sendMessage(chat_id=chat_id, text="코인 자동 매매가 {0}분 동안 작동 중입니다.".format(index))
    index += 10
    time.sleep(600) # 십분에 한번씩

