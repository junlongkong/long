from utils import config
import dolphindb as ddb
import pandas as pd
import numpy as np

s = ddb.session()
s.connect("127.0.0.1",8848,"admin","123456")

i =0
while(i<1):
    s.run("data = select '210210.IB', now(), 0.1, 1000 from Trade")
    s.run("tableInsert(Trade,data)")
    i = i +1
# j =0
# while(j<5):
#     s.run("data = select '000002', now(), 0.88, 1200 from Trade")
#     s.run("tableInsert(Trade,data)")
#     j = j +1

