import dolphindb as ddb
import pandas as pd
import numpy as np

csv_file = "./trades.csv"
csv_data = pd.read_csv(csv_file, dtype={'Symbol':str})
csv_df = pd.DataFrame(csv_data)
s = ddb.session()
s.connect("127.0.0.1",8848,"admin","123456")
#上传DataFrame到DolphinDB，并对Datetime字段做类型转换
s.upload({"tmpData":csv_df})
s.run("data = select Symbol, datetime(Datetime) as Datetime, Price, Volume from tmpData")
s.run("tableInsert(Trade,data)")