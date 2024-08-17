from utils import config
import dolphindb as ddb
import pandas as pd
import numpy as np

s = ddb.session()
s.connect("127.0.0.1",8848,"admin","123456")

#x是数据，3是滑动窗口大小，warmup是否需要预热
s.run("x=12.1 12.2 12.6 12.8 11.9 11.6 11.2")
no_warm_up = s.run("ema(x,3, warmup=false)")
print(no_warm_up)
warm_up = s.run("ema(x,3, warmup=true)")
print(warm_up)

