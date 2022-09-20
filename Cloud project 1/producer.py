import boto3
import json
import logging
import json
import boto3
import sys
from gpg import Data
import yfinance as yf
import numpy as np
STREAM_NAME = "CloudFormationProject1"
import time
import random
import datetime
import pandas as pd
from ast import literal_eval

logging.basicConfig(level = logging.INFO)

session = boto3.Session(region_name='us-east-1')
client = session.client('kinesis')
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(2)
#test_data = {'gamer_tag': 'JoeGamer', 'score': '100', 'character': 'Flame Warrior'}
tickerlist={"MSFT","MVIS","GOOG","SPOT","INO","OCGN","ABML","RLLCF","JNJ","PSFE"}
df_list = list()
for ticker in tickerlist:
    data = yf.download(ticker, start=yesterday, end=today, interval = "1h")
    ticker_info=yf.Ticker(ticker).info
  #  print(ticker_info['fiftyTwoWeekHigh'])
    for value in data.iterrows():

        record = {'open': value[1]['Open'], 'high': value[1]['High'], 'low': value[1]['Low'],'close': value[1]['Close'], 'ts':value[0].strftime('%Y-%m-%d %H:%M:%S'), 'name': ticker,'52WeekHigh':ticker_info['fiftyTwoWeekHigh'],'52WeelkLow':ticker_info['fiftyTwoWeekLow']}
      #  print(record)
        #Snew_dict={'open': value[1]['Open'], 'high': value[1]['High'], 'low': value[1]['Low'],'close': value[1]['Close'], 'ts':value[0].strftime('%Y-%m-%d %H:%M:%S'), 'name': ticker}
        as_jsonstr = json.dumps(record)
        Inputdata = json.loads(as_jsonstr)
        response = client.put_record(
        StreamName='CloudFormationProject1',
        Data=as_jsonstr,
        PartitionKey=ticker
        )
        print(response)




logging.info("stock details: %s", as_jsonstr)