from utils import config
import dolphindb as ddb
import pandas as pd
import numpy as np

s = ddb.session()
s.connect("127.0.0.1",8848,"admin","123456")


# i =0
# while(i<5):
#     s.run("data = select now(),'BTC', 'Spot', 2000, 'kongjunlong' from position")
#     s.run("tableInsert(position,data)")
#     i = i +1
#
#
# j =0
# while(j<5):
#     s.run("data = select now(),'BTC-USDT', 70000 from position")
#     s.run("tableInsert(market,data)")
#     j = j +1
#
# t=0
# while(t<5):
#     s.run("data = select now(),'BTC', 'bybit-001', 1000, 'kongjunlong' from position")
#     s.run("tableInsert(fund,data)")
#     t = t +1


ii =0
while(ii<5000):
    s.run("data = select now(),'BTC', 'Spot', 2000, 'kongjunlong' from positionHistory")
    s.run("tableInsert(positionHistory,data)")
    ii = ii +1
s.run("data = select now(),'BTC', 'Spot', 2000, 'kongjunlong' from positionHistory")
s.run("tableInsert(positionHistory,data)")
