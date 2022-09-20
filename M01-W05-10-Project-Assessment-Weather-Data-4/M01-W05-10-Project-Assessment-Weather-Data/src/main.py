from model import DailyReportModel, UserModel, DeviceModel, WeatherDataModel
from datetime import datetime
import json
import pandas as pd

# Shows how to initiate and search in the users collection based on a username
print("======================= Search User Details======================================================================")
user_coll = UserModel()
username = input("Please enter the username : ")
user_document = user_coll.find_by_username(username)
if (user_document):
    print(user_document)
    print("=========================================================================================================")
# Shows a successful attempt on how to insert a user
print("============================Success Scenario | User Addition =================================================================")
username = input("Please enter the login name : ")
user_document = user_coll.insert('test_3', 'test_3@example.com', 'default',username)
if (user_document == -1):
    print(user_coll.latest_error)
    print("============================================================================================================")
else:
    print(user_document)
    print("=========================================================================================================")

# Shows a failure attempt on how to insert a user
print("============================Failure Scenario | User Addition =================================================================")
username = input("Please enter the login name : ")
user_document = user_coll.insert('test_3', 'test_3@example.com', 'default',username)
if (user_document == -1):
    print(user_coll.latest_error)
    print("============================================================================================================")
else:
    print(user_document)
    print("===========================================================================================================")

# Shows how to initiate and search in the devices collection based on a device id
print("==================================Search Device Details===========================================================")
device_coll = DeviceModel()
device_document = device_coll.find_by_device_id('DT002')
if (device_document):
    print(device_document)
    print("==================================================================================================================")

# Shows a successful attempt on how to insert a new device
print("========================Success scenario Of Device Insertion=====================================================================")
print("Pass proper user info for successful creation| User Id :admin[only have insert permission] " )
username = input("Please enter the username : ")
device_document = device_coll.insert('DT203', 'Temperature Sensor', 'Temperature', 'Acme',username)
if (device_document == -1):
    print(device_coll.latest_error)
    print("=======================================================================================================================")
else:
    print(device_document)
    print("=======================================================================================================================")

# Shows a failure attempt on how to insert a new device
print("========================Failure Scenario  | Device Insertion=====================================================================")
username = input("Please enter the username : ")
device_document = device_coll.update('DT002', 'desc', 'Temperature0008',username)
if (device_document == -1):
    print(device_coll.latest_error)
    print("=======================================================================================================================")
else:
    print(device_document)
    print("=======================================================================================================================")

# Shows a successful attempt on how to update a  device
print("========================Success scenario Of Device Detail Updation=====================================================================")
print("Pass proper user info inorder to perform a successful updation| User Id :admin|user_2 hav R/W access for DT devices | admin|user_1 hav R/W access for DH devices" )
username = input("Please enter the username : ")
device_id = input("Please enter the device id : ")
field_name = input("Please enter the feild name to modified or to be updated : ")
value_tobe_updated = input("Please enter the feild value to modified or to be updated : ")
device_document = device_coll.update(device_id, field_name, value_tobe_updated, username)
if (device_document == -1):
    print(device_coll.latest_error)
    print("=======================================================================================================================")
else:
    print("updated value: ")
    print(device_document)
    print("=======================================================================================================================")
# show Failure scenario of device details updation
# Shows a successful attempt on how to update a  device
print("========================Success scenario Of Device Detail Updation=====================================================================")
print("Pass proper user info inorder to perform a successful updation| User Id :admin|user_2 hav R/W access for DT devices | admin|user_1 hav R/W access for DH devices" )
username = input("Please enter the username : ")
device_id = input("Please enter the device id : ")
field_name = input("Please enter the feild name to modified or to be updated : ")
value_tobe_updated = input("Please enter the feild value to modified or to be updated : ")
device_document = device_coll.update(device_id, field_name, value_tobe_updated, username)
if (device_document == -1):
    print(device_coll.latest_error)
    print("=======================================================================================================================")
else:
    print("updated value: ")
    print(device_document)
    print("=======================================================================================================================")



# Shows how to initiate and search in the weather_data collection based on a device_id and timestamp
print("================================Search Weather Details=============================================================")
wdata_coll = WeatherDataModel()
wdata_document = wdata_coll.find_by_device_id_and_timestamp('DT002', datetime(2020, 12, 2, 13, 30, 0))
if (wdata_document):
    
    print(wdata_document)
    print("============================================================================================================")

# Shows a success attempt on how to insert a new data point
print("=======================Success Scenario Of Weather Data Insertion======================================================================")
username = input("Please enter the login name : ")
wdata_document = wdata_coll.insert('DT002', 12, datetime(2020, 12, 2, 13, 38, 0),username)
if (wdata_document == -1):
    print(wdata_coll.latest_error)
    print("=============================================================================================================================")
else:
    print(wdata_document)
    print("=============================================================================================================================")
# Shows a failed attempt on how to insert a new data point4
print("=======================Failure scenario Of Weather Data Insertion======================================================================")
username = input("Please enter the login name : ")
wdata_col2 = WeatherDataModel()
wdata_document = wdata_col2.insert('DT002', 12, datetime(2020, 12, 1, 13, 30, 0),username)
if (wdata_document == -1):
    print(wdata_col2.latest_error)
    print("=============================================================================================================================")
else:
    print(wdata_document)
    print("=============================================================================================================================")

# Shows a success attempt on how to update a  data point
print("=======================Success Scenario Of Weather Data update======================================================================")
print("please pass proper timestamp and device id | user_id with update access are admin and user_2")
username = input("Please enter the login name : ")
username = input("Please enter the login name : ")
device_id = input("Please enter the device id : ")
db_timestamp = input("Please enter the timestamp [Note: Device id and timestamp combination should be present  in collection]Format of input is datetime(2020, 12, 1, 00, 38, 0) : ")
field_name = input("Please enter the feild name to modified or to be updated : ")
value_tobe_updated = input("Please enter the feild value to modified or to be updated : ")
wdata_document = wdata_coll.update(device_id, db_timestamp, field_name, value_tobe_updated,username)
if (wdata_document == -1):
    print(wdata_coll.latest_error)
    print("=============================================================================================================================")
else:
    print("Updated weather details : ")
    print(wdata_document)
    print("=============================================================================================================================")

# Shows a Failure attempt on how to update a  data point
print("=======================Failure Scenario Of Weather Data update======================================================================")
print("please pass proper timestamp | device id[DT002] | For DT devices admin and user_2 have R/W access|User_1 has R/W access for DH devices")
username = input("Please enter the login name : ")
device_id = input("Please enter the device id : ")
db_timestamp = input("Please enter the timestamp [Note: Device id and timestamp combination should be present  in collection]Format of input is datetime(2020, 12, 1, 00, 38, 0) : ")
field_name = input("Please enter the feild name to modified or to br updated : ")
value_tobe_updated = input("Please enter the feild name to modified or to br updated : ")
wdata_document = wdata_coll.update(device_id, db_timestamp, field_name, value_tobe_updated,username)
if (wdata_document == -1):
    print(wdata_coll.latest_error)
    print("=============================================================================================================================")
else:
    print("Updated weather details : ")
    print(wdata_document)
    print("=============================================================================================================================")
# fetching data from daily_report collection based on device id and  day
print("============fetching data from daily_report collection based on device id and day ===================================")
print("please enter device id and day for the data fetch :")
device_id = input("Please enter the device id : ")
day = input("Please enter the  day : ")
DAILY_REPORT_COLLECTION = 'daily_reports'
daily_report_coll = DailyReportModel()
daily_report_document = daily_report_coll.find_by_device_id_and_day(device_id,day)

if (daily_report_document == -1):
    print(daily_report_coll.latest_error)
    print("=============================================================================================================================")
else:
    print("Updated weather details : ")
    print(daily_report_document)
    print("=============================================================================================================================")

# fetching data from daily_report collection based on device id and range of days
print("============fetching data from daily_report collection based on device id and range of days===================================")
print("please enter device id and range of days for the data fetch :")
device_id = input("Please enter the device id : ")
starting_day = input("Please enter the starting day : ")
end_day = input("Please enter the end day : ")

daily_report_coll = DailyReportModel()
daily_report_document = daily_report_coll.fetchData(starting_day,end_day,device_id)

if (daily_report_document == -1):
    print(daily_report_coll.latest_error)
    print("=============================================================================================================================")
else:
    print("Report details : ")
    print(list(daily_report_document))
    print("=============================================================================================================================")
