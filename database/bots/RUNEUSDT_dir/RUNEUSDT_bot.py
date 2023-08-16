# from binance.client import Client
import os
from datetime import datetime
from binance.client import Client
from cryptography.fernet import Fernet
import pandas as pd
import time
from math import fabs

def get_symbol_name():
    return os.path.basename(__file__).split("_")[0]

def get_balance_bot(name):
    with open (f"database/bots/{name}_dir/{name}_bot_balance_now.txt" ,"r") as file:
    
      balance_bot = file.read()  
    return balance_bot

# Получение api бинанс
def get_api_binance():
    with open("database/ApiData.txt", "r") as file:
        first_lale = file.readline()
        list_split = first_lale.split(" ")[0].split("'")
        secret_key = get_secretKey()
        fernet = Fernet(secret_key)
     
        return fernet.decrypt(bytes(list_split[1].encode('utf-8'))).decode('utf-8'), fernet.decrypt(bytes(list_split[3].encode('utf-8'))).decode('utf-8')
#    получение секретного ключа из файла для дешифпрвки
def get_secretKey():
    with open("database/key.txt", "r") as file:
        first_lale = file.readline()
        
        return first_lale  
    
    # Проверка веремени 
def checkTime():
    time = datetime.now()
    sec,minute = time.second,time.minute
    if (str(minute)=="59"  or str(minute)=="14" or str(minute)=="29" or str(minute)=="44") and 58<=int(sec)<=59:
        
        return True
    else:
        
        return False
# непрерывная проверка вермени 
def checkTime_all():
    while True:
        if checkTime():
            print("Свечка подошла")
            print(datetime.now())
            return True
            
        else:
            
            continue

# Проверка есть ли сделка в данный помент
def check_deals_in_trade(client, symbol):
    positions = client.futures_account()["positions"]
    for position in positions:
        if position['symbol'] == symbol and float(position['initialMargin']) > 0 and float(position['positionAmt']) != 0:
            print("Ты в позиции")
            return True
    return False 


# Получение свечек 
def last_data(client, symbol, interval, lookback):
    frame = pd.DataFrame(client.futures_historical_klines(symbol,interval,lookback+'min ago UTC'))
    frame = frame.iloc[:,:-6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index,unit='ms')
    frame = frame.astype(float)
    
    print(frame)
    return frame

def checkCandle(Open,Close):
    procent=fabs(Open-Close)*100/Open
    pos =''
    if  Open<Close:
        pos = True
    else:
        pos = False
    return procent,pos

# client = Client("IC5q1H8RKPs91Foub0qeKnnX9PMD46buZlf01LLnuDgFOCpEBhJiA34knHXaIoun","0Kq5Btdep4O67sLxOrQXrpKdE4TcSpRn8uRoaATbm28R4csBuO4h53jHn5H9rSYU")
# symbol = 'XRPUSDT' 
# # deals = client.futures_account_trades(symbol = "XRPUSDT") 
# ticker = client.futures_ticker(symbol = symbol)
# print(float(ticker["priceChange"]))

def check_three_candle(procent1 , pos1, procent2 , pos2, procent3 , pos3):
    if (pos1 and pos2 and pos3) and (procent1>=0.15 and procent2>=0.15 and procent3>=0.15):
        return "SHORT"
    
    if (not pos1 and not pos2 and not pos3) and (procent1>=0.15 and procent2>=0.15 and procent3>=0.15):
        return "LONG"
    else:
        return False
# Округление для подсчёта стоп лимиток
def check_numRound(price):
    return len(str(price).split(".")[1])

def strategy(client,symbol, balance):
    try:
        candle = last_data(client, symbol,'15m','45')
        
    except:
        time.sleep(1)
        print("Пойманная ошибка")
        candle = last_data(client, symbol,'15m','45')
    time.sleep(1)
    open_1,close_1 = candle.Open.iloc[-3], candle.Close.iloc[-3]
    open_2,close_2 = candle.Open.iloc[-2], candle.Close.iloc[-2]
    open_3,close_3 = candle.Open.iloc[-1], candle.Close.iloc[-1]
    procent1 , pos1 = checkCandle(open_1,close_1)
    procent2 , pos2 = checkCandle(open_2,close_2)
    procent3 , pos3 = checkCandle(open_3,close_3)
    
    check_candle = check_three_candle(procent1 , pos1, procent2 , pos2, procent3 , pos3)
    qty = int(round(balance/candle.Close.iloc[-1],1))
    # ..........................................................
    # Для захода в шорт
    if check_candle == "SHORT":
        buyprice =close_1
        round_price = check_numRound(buyprice)
        catch_error = False 
        try:
            client.futures_create_order(symbol = symbol,side="SELL",type = "MARKET",quantity = qty)
            catch_error = True
            print(f"Заход в шорт по монете {symbol}")
            
            tP_S,sL_S = 0.9975, 1.002
            
            client.futures_create_order(symbol = symbol,side="BUY",type = "STOP_MARKET",timeInForce='GTE_GTC',quantity = qty,stopPrice=round(buyprice*sL_S,round_price))
            print(f"SL Потавлен по ставлен по монете{symbol}")
            
            client.futures_create_order(symbol = symbol,side="BUY",type = "TAKE_PROFIT_MARKET",timeInForce='GTE_GTC',quantity = qty,stopPrice=round(buyprice*tP_S,round_price))
            print(f"TP Потавлен по ставлен по монете{symbol}")

            catch_error = False
        except Exception as e:
            print(e)
            
            if catch_error:
                client.futures_create_order(symbol = symbol,side="BUY",type = "MARKET",quantity = qty)
                client.futures_cancel_all_open_orders(symbol=symbol)
                return 0 
            else:
                return 0 
    # ..........................................................
    # Для захода в лонг
    if check_candle == "LONG":
        buyprice =close_1
        round_price = check_numRound(buyprice)
        catch_error = False 
        try:
            client.futures_create_order(symbol = symbol,side="SELL",type = "MARKET",quantity = qty)
            catch_error = True
            print(f"Заход в шорт по монете {symbol}")
            
            tP_S,sL_S = 1.0025, 0.998
            
            client.futures_create_order(symbol = symbol,side="BUY",type = "TAKE_PROFIT_MARKET",timeInForce='GTE_GTC',quantity = qty,stopPrice=round(buyprice*sL_S,round_price))
            print(f"SL Потавлен по ставлен по монете{symbol}")
            
            client.futures_create_order(symbol = symbol,side="BUY",type = "STOP_MARKET",timeInForce='GTE_GTC',quantity = qty,stopPrice=round(buyprice*tP_S,round_price))
            print(f"TP Потавлен по ставлен по монете{symbol}")

            catch_error = False
        except Exception as e:
            print(e)
            
            if catch_error:
                client.futures_create_order(symbol = symbol,side="BUY",type = "MARKET",quantity = qty)
                client.futures_cancel_all_open_orders(symbol=symbol)
                return 0 
            else:
                return 0 

    else:
        return 0

def strategy_start(client,symbol,balance):
    while True:
    
        if checkTime_all():
            if not check_deals_in_trade(client, symbol):
                strategy(client, symbol, balance)
            else:
                continue
        else:
            continue

api, secret = get_api_binance()
client = Client(api,secret)
symbol_name = get_symbol_name()
balance_bot = (float(get_balance_bot(symbol_name))*90)/100








strategy_start(client, symbol_name, balance_bot, )

# client.futures_create_order(symbol = symbol_name,side="SELL",type = "MARKET",quantity = 30)
# print(last_data(client, symbol_name,'15m','45'))