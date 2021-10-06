import pyupbit
import time

access = "tmobuBWWxvYxV9B2oW8ewuv0VsRZXEj8NIApk1Qn" 
secret = "xPbZVoYxzeuDkmh9aQPJlQqxn9S6sg1edb8YnEP8" 
upbit = pyupbit.Upbit(access, secret)

while True:
        if upbit.get_balance("KRW-ETH") > 0.00001 :   
                if upbit.get_avg_buy_price("KRW-ETH")*0.95 > pyupbit.get_current_price("KRW-ETH"): # 2. 이더리움을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if upbit.get_balance("KRW") > 100000:
                        upbit.buy_market_order("KRW-ETH", upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상인 경우 잔고의 5% 매수
                    elif upbit.get_balance("KRW") > 50000:
                        upbit.buy_market_order("KRW-ETH", upbit.get_balance("KRW")*0.1)# 2-2. 잔고가 5만원 이상인 경우 잔고의 10% 매수
                    elif upbit.get_balance("KRW") > 20000:
                        upbit.buy_market_order("KRW-ETH", upbit.get_balance("KRW")*0.3)# 2-3. 잔고가 2만원 이상인 경우 잔고의 30% 매수
                    elif upbit.get_balance("KRW") > 10000:
                        upbit.buy_market_order("KRW-ETH", upbit.get_balance("KRW")*0.9)# 2-4. 잔고가 만원 이상인 경우 잔고의 90% 매수
  
                elif upbit.get_avg_buy_price("KRW-ETH")*2 < pyupbit.get_current_price("KRW-ETH"):# 2. 이더리움 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                 upbit.sell_market_order("KRW-ETH",upbit.get_balance("KRW-ETH"))   
    
                elif upbit.get_avg_buy_price("KRW-ETH")*1.05 < pyupbit.get_current_price("KRW-ETH"):# 1. 이더리움 현재 가격이 구매 가격보다 5% 높고, 
                    if upbit.get_balance("KRW-ETH")*pyupbit.get_current_price("KRW-ETH") > (upbit.get_balance("KRW-ETH")*pyupbit.get_current_price("KRW-ETH") + upbit.get_balance("KRW-ETC")*pyupbit.get_current_price("KRW-ETC") + upbit.get_balance("KRW-BTC")*pyupbit.get_current_price("KRW-BTC") + upbit.get_balance("KRW-DOT")*pyupbit.get_current_price("KRW-DOT") + upbit.get_balance("KRW-DOGE")*pyupbit.get_current_price("KRW-DOGE") + upbit.get_balance("KRW"))*0.05: # 보유금액이 총 금액의5%보다 높은 경우, 보유분의 5% 매도
                     upbit.sell_market_order("KRW-ETH", upbit.get_balance("KRW-ETH")*0.05)  
        else : 
                upbit.buy_market_order("KRW-ETH", upbit.get_balance("KRW")*0.05) # 1. 이더리움을 보유하지 않는 경우, 잔고의 5% 매수

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

        if upbit.get_balance("KRW-BTC") > 0.0000000000001 :   
                if upbit.get_avg_buy_price("KRW-BTC")*0.95 > pyupbit.get_current_price("KRW-BTC"): # 2. 비트코인을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if upbit.get_balance("KRW") > 100000:
                        upbit.buy_market_order("KRW-BTC", upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상인 경우 잔고의 5% 매수
                    elif upbit.get_balance("KRW") > 50000:
                        upbit.buy_market_order("KRW-BTC", upbit.get_balance("KRW")*0.1)# 2-2. 잔고가 5만원 이상인 경우 잔고의 10% 매수
                    elif upbit.get_balance("KRW") > 20000:
                        upbit.buy_market_order("KRW-BTC", upbit.get_balance("KRW")*0.3)# 2-3. 잔고가 2만원 이상인 경우 잔고의 30% 매수
                    elif upbit.get_balance("KRW") > 10000:
                        upbit.buy_market_order("KRW-BTC", upbit.get_balance("KRW")*0.9)# 2-4. 잔고가 만원 이상인 경우 잔고의 90% 매수
  
                elif upbit.get_avg_buy_price("KRW-BTC")*2 < pyupbit.get_current_price("KRW-BTC"):# 2. 비트코인 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                 upbit.sell_market_order("KRW-BTC",upbit.get_balance("KRW-BTC"))   
    
                elif upbit.get_avg_buy_price("KRW-BTC")*1.05 < pyupbit.get_current_price("KRW-BTC"):# 1. 비트코인 현재 가격이 구매 가격보다 5% 높고, 
                    if upbit.get_balance("KRW-BTC")*pyupbit.get_current_price("KRW-BTC") > (upbit.get_balance("KRW-ETH")*pyupbit.get_current_price("KRW-ETH") + upbit.get_balance("KRW-ETC")*pyupbit.get_current_price("KRW-ETC") + upbit.get_balance("KRW-BTC")*pyupbit.get_current_price("KRW-BTC") + upbit.get_balance("KRW-DOT")*pyupbit.get_current_price("KRW-DOT") + upbit.get_balance("KRW-DOGE")*pyupbit.get_current_price("KRW-DOGE") + upbit.get_balance("KRW"))*0.05: # 보유금액이 총 금액의5%보다 높은 경우, 보유분의 5% 매도
                     upbit.sell_market_order("KRW-BTC", upbit.get_balance("KRW-BTC")*0.05)  
        else : 
                upbit.buy_market_order("KRW-BTC", upbit.get_balance("KRW")*0.05) # 1. 비트코인을 보유하지 않는 경우, 잔고의 5% 매수

        if upbit.get_balance("KRW-DOT") > 0.0000000000001 :   
                if upbit.get_avg_buy_price("KRW-DOT")*0.95 > pyupbit.get_current_price("KRW-DOT"): # 2. 폴카닷을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if upbit.get_balance("KRW") > 100000:
                        upbit.buy_market_order("KRW-DOT", upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상인 경우 잔고의 5% 매수
                    elif upbit.get_balance("KRW") > 50000:
                        upbit.buy_market_order("KRW-DOT", upbit.get_balance("KRW")*0.1)# 2-2. 잔고가 5만원 이상인 경우 잔고의 10% 매수
                    elif upbit.get_balance("KRW") > 20000:
                        upbit.buy_market_order("KRW-DOT", upbit.get_balance("KRW")*0.3)# 2-3. 잔고가 2만원 이상인 경우 잔고의 30% 매수
                    elif upbit.get_balance("KRW") > 10000:
                        upbit.buy_market_order("KRW-DOT", upbit.get_balance("KRW")*0.9)# 2-4. 잔고가 만원 이상인 경우 잔고의 90% 매수
  
                elif upbit.get_avg_buy_price("KRW-DOT")*2 < pyupbit.get_current_price("KRW-DOT"):# 2. 폴카닷 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                 upbit.sell_market_order("KRW-DOT",upbit.get_balance("KRW-DOT"))   
    
                elif upbit.get_avg_buy_price("KRW-DOT")*1.05 < pyupbit.get_current_price("KRW-DOT"):# 1. 폴카닷 현재 가격이 구매 가격보다 5% 높고, 
                    if upbit.get_balance("KRW-DOT")*pyupbit.get_current_price("KRW-DOT") > (upbit.get_balance("KRW-ETH")*pyupbit.get_current_price("KRW-ETH") + upbit.get_balance("KRW-ETC")*pyupbit.get_current_price("KRW-ETC") + upbit.get_balance("KRW-BTC")*pyupbit.get_current_price("KRW-BTC") + upbit.get_balance("KRW-DOT")*pyupbit.get_current_price("KRW-DOT") + upbit.get_balance("KRW-DOGE")*pyupbit.get_current_price("KRW-DOGE") + upbit.get_balance("KRW"))*0.05: # 보유금액이 총 금액의5%보다 높은 경우, 보유분의 5% 매도
                     upbit.sell_market_order("KRW-DOT", upbit.get_balance("KRW-DOT")*0.05)  
        else : 
                upbit.buy_market_order("KRW-DOT", upbit.get_balance("KRW")*0.05) # 1. 폴카닷을 보유하지 않는 경우, 잔고의 5% 매수

        if upbit.get_balance("KRW-DOGE") > 0.0000000000001 :   
                if upbit.get_avg_buy_price("KRW-DOGE")*0.95 > pyupbit.get_current_price("KRW-DOGE"): # 2. 도지을 보유면서, 현재 가격이 구매 가격보다 5% 낮은 경우,  
                    if upbit.get_balance("KRW") > 100000:
                        upbit.buy_market_order("KRW-DOGE", upbit.get_balance("KRW")*0.05)# 2-1. 잔고가 10만원 이상인 경우 잔고의 5% 매수
                    elif upbit.get_balance("KRW") > 50000:
                        upbit.buy_market_order("KRW-DOGE", upbit.get_balance("KRW")*0.1)# 2-2. 잔고가 5만원 이상인 경우 잔고의 10% 매수
                    elif upbit.get_balance("KRW") > 20000:
                        upbit.buy_market_order("KRW-DOGE", upbit.get_balance("KRW")*0.3)# 2-3. 잔고가 2만원 이상인 경우 잔고의 30% 매수
                    elif upbit.get_balance("KRW") > 10000:
                        upbit.buy_market_order("KRW-DOGE", upbit.get_balance("KRW")*0.9)# 2-4. 잔고가 만원 이상인 경우 잔고의 90% 매수
  
                elif upbit.get_avg_buy_price("KRW-DOGE")*2 < pyupbit.get_current_price("KRW-DOGE"):# 2. 도지 현재 가격이 구매 가격보다 100% 높은 경우, 전량 판매
                 upbit.sell_market_order("KRW-DOGE",upbit.get_balance("KRW-DOGE"))   
    
                elif upbit.get_avg_buy_price("KRW-DOGE")*1.05 < pyupbit.get_current_price("KRW-DOGE"):# 1. 도지 현재 가격이 구매 가격보다 5% 높고, 
                    if upbit.get_balance("KRW-DOGE")*pyupbit.get_current_price("KRW-DOGE") > (upbit.get_balance("KRW-ETH")*pyupbit.get_current_price("KRW-ETH") + upbit.get_balance("KRW-ETC")*pyupbit.get_current_price("KRW-ETC") + upbit.get_balance("KRW-BTC")*pyupbit.get_current_price("KRW-BTC") + upbit.get_balance("KRW-DOT")*pyupbit.get_current_price("KRW-DOT") + upbit.get_balance("KRW-DOGE")*pyupbit.get_current_price("KRW-DOGE") + upbit.get_balance("KRW"))*0.05: # 보유금액이 총 금액의5%보다 높은 경우, 보유분의 5% 매도
                     upbit.sell_market_order("KRW-DOGE", upbit.get_balance("KRW-DOGE")*0.05)  
        else : 
                upbit.buy_market_order("KRW-DOGE", upbit.get_balance("KRW")*0.05) # 1. 이도지 보유하지 않는 경우, 잔고의 5% 매수

        time.sleep(1800) # 위의 명령은 매 반시간마다 적용
