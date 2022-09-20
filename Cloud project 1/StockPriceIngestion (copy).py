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


# Your goal is to get per-hour stock price data for a time range for the ten stocks specified in the doc. 
# Further, you should call the static info api for the stocks to get their current 52WeekHigh and 52WeekLow values.
# You should craft individual data records with information about the stockid, price, price timestamp, 52WeekHigh and 52WeekLow values and push them individually on the Kinesis stream

kinesis_client = boto3.client('kinesis', region_name = "us-east-1") #Modify this line of code according to your requirement.

today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(2)

# Example of pulling the data between 2 dates from yfinance API
#data = yf.download("MSFT MVIS GOOG SPOT INO OCGN ABML RLLCF JNJ PSFE", start= yesterday, end= today, interval = '1h',group_by='tickers' )

## Add code to pull the data for the stocks specified in the doc


## Add additional code to call 'info' API to get 52WeekHigh and 52WeekLow refering this this link - https://pypi.org/project/yfinance/


## Add your code here to push data records to Kinesis stream.
def get_data(stock):
    df = yf.download(stock, start=yesterday, end=today,group_by="ticker", interval = "1h") 
    #df = df.stack(level=0).rename_axis(['Date' ]).reset_index(level=1)
    return df

  

def generate(stream_name, kinesis_client):
    
    tickerlist={"MSFT","MVIS","GOOG","SPOT","INO","OCGN","ABML","RLLCF","JNJ","PSFE"}
    
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
            response = kinesis_client.put_record(
            StreamName='CloudFormationProject1',
            Data=as_jsonstr,
            PartitionKey=ticker
            )
            print(response)




           
if __name__ == '__main__':        
    
    
    generate(stream_name='CloudFormationProject1', kinesis_client=boto3.client('kinesis'))