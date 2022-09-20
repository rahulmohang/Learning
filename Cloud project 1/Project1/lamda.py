from pprint import pprint
import boto3
import json
import csv
import datetime
import os
import random
import base64
from decimal import Decimal
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    
    AWS_REGION = 'us-east-1'
    #print(event)
    
    dynamodb_res = boto3.resource('dynamodb', region_name=AWS_REGION)
    anomaly_table = dynamodb_res.Table('POIDetails')

    sns_client = boto3.client('sns', region_name=AWS_REGION)
    topic_arn = "arn:aws:sns:us-east-1:005816983450:stockPOI"

    for record in event['Records']:
        data_point = base64.b64decode(record['kinesis']['data'])
        data_point = str(data_point, 'utf-8')
        pprint(data_point, sort_dicts=False)
        data_point = json.loads(data_point)
        if(data_point['Records']):
            print (data_point)
            fiftyTwoWeekHigh=data_point['Records']['52WeekHigh']
            fiftyTwoWeekLow=data_point['Records']['52WeekLow']
            openvalue=data_point['Records']['open']
            closevalue= data_point['Records']['close']
            ticker= data_point['Records']['name']
            if(closevalue>=(80 % fiftyTwoWeekHigh) or closevalue (99 % fiftyTwoWeekLow)):
                POI = True		
                print("Point Of Intrest " +ticker )
            else:
                POI = False
            if(POI):
                dynamodb_res = boto3.resource('dynamodb', region_name='us-east-1')
                table = dynamodb_res.Table('POIDetails')
                InsertPOIdata = {
                    'fiftyTwoWeekHigh' : data_point['Records']['52WeekHigh'],
                    'fiftyTwoWeekLow' : data_point['Records']['52WeekLow'],
                    'openvalue' : data_point['Records']['open'],
                    'closevalue' : data_point['Records']['close'],
                    'name': data_point['Records']['name'],
                    'ts' : data_point['Records']['ts']}
                POI_data = json.loads(json.dumps( InsertPOIdata ), parse_float=Decimal)
                response = table.put_item(Item= InsertPOIdata)
                print("POI Data inserted to DynamoDb")
               
                sns_client.publish(TopicArn=topic_arn, 
                            Message=str("POI Details = " + str(InsertPOIdata['value']) + " is POI detected. " ,
                            Subject=str(InsertPOIdata['name'] + " POI is detected for this stock.")
                            ))
    return 1