# Imports Database class from the project to provide basic functionality for database access
from database import Database
# Imports ObjectId to convert to the correct format before querying in the db
from bson.objectid import ObjectId
import json

from setup import DAILY_REPORT_COLLECTION

# User document contains username (String), email (String), and role (String) fields
class UserModel:
    USER_COLLECTION = 'users'

    def __init__(self):
        self._db = Database()
        self._latest_error = ''
    
    # Latest error is used to store the error string in case an issue. It's reset at the beginning of a new function call
    @property
    def latest_error(self):
        return self._latest_error
    
    # Since username should be unique in users collection, this provides a way to fetch the user document based on the username
    def find_by_username(self, username):
        key = {'username': username}
        return self.__find(key)
    
    # Finds a document based on the unique auto-generated MongoDB object id 
    def find_by_object_id(self, obj_id):
        key = {'_id': ObjectId(obj_id)}
        return self.__find(key)
    
    # Private function (starting with __) to be used as the base for all find functions
    def __find(self, key):
        user_document = self._db.get_single_data(UserModel.USER_COLLECTION, key)
        return user_document
    
    # This first checks if a user already exists with that username. If it does, it populates latest_error and returns -1
    # If a user doesn't already exist, it'll insert a new document and return the same to the caller
    def insert(self, username, email, role,Loginname):
        self._latest_error = ''
        user_document = self.find_by_username(Loginname)
        if (user_document):
            if (Loginname == "admin"):
                user_document = self.find_by_username(username)
                if (user_document):
                    self._latest_error = f'Username {username} already exists'
                    return -1
                user_data = {'username': username, 'email': email, 'role': role}
                user_obj_id = self._db.insert_single_data(UserModel.USER_COLLECTION, user_data)
                return self.find_by_object_id(user_obj_id)
            else:
                print(Loginname+" dont have write access in User ollection")
        else: 
            self._latest_error = f'Username {Loginname} not exists'
            return -1
       

# Device document contains device_id (String), desc (String), type (String - temperature/humidity) and manufacturer (String) fields
class DeviceModel:
    DEVICE_COLLECTION = 'devices'

    def __init__(self):
        self._db = Database()
        self._latest_error = ''
    
    # Latest error is used to store the error string in case an issue. It's reset at the beginning of a new function call
    @property
    def latest_error(self):
        return self._latest_error
    
    # Since device id should be unique in devices collection, this provides a way to fetch the device document based on the device id
    def find_by_device_id(self, device_id):
        key = {'device_id': device_id}
        return self.__find(key)
    
    # Finds a document based on the unique auto-generated MongoDB object id 
    def find_by_object_id(self, obj_id):
        key = {'_id': ObjectId(obj_id)}
        return self.__find(key)
    
    # Private function (starting with __) to be used as the base for all find functions
    def __find(self, key):
        device_document = self._db.get_single_data(DeviceModel.DEVICE_COLLECTION, key)
        return device_document
    
    # This first checks if a device already exists with that device id. If it does, it populates latest_error and returns -1
    # If a device doesn't already exist, it'll insert a new document and return the same to the caller
    def insert(self, device_id, desc, type, manufacturer, username):
        self._latest_error = ''
        device_document = self.find_by_device_id(device_id)
        if (device_document):
            self._latest_error = f'Device id {device_id} already exists'
            return -1
        Userdetails = UserModel()
        Userdtls = Userdetails.find_by_username(username)
        if (Userdtls):
            if (Userdtls['role'] == "admin"):
                device_data = {'device_id': device_id, 'desc': desc, 'type': type, 'manufacturer': manufacturer}
                device_obj_id = self._db.insert_single_data(DeviceModel.DEVICE_COLLECTION, device_data)
                return self.find_by_object_id(device_obj_id)
            else: 
                device_exception = Userdtls['device_exception'].split("_")
                for i in device_exception:
                    if (Userdtls['device_exception'] == i):
                        device_data = {'device_id': device_id, 'desc': desc, 'type': type, 'manufacturer': manufacturer}
                        device_obj_id = self._db.insert_single_data(DeviceModel.DEVICE_COLLECTION, device_data)
                        return self.find_by_object_id(device_obj_id)
                    else:
                        print(username+" don't have write access in Device DB")
        else:
            self._latest_error = f'User id {username} is invalid'
            return -1
      # This is to make update to a device document.
    def update(self, device_id, field, field_value, username):
        self._latest_error = ''
        device_document = self.find_by_device_id(device_id)
        if (device_document):
            id = device_document['_id']
            Userdetails = UserModel()
            Userdtls = Userdetails.find_by_username(username)
            if (Userdtls):
                if (Userdtls['role'] == "admin"):
                    device_updated_details = self._db.update_single_data(DeviceModel.DEVICE_COLLECTION,id,field,field_value)
                    return device_updated_details
                else: 
                    device_exception = Userdtls['device_exception']
                    devices=device_exception.split("_")
                    for i in devices:
                        if(i==device_id):
                            print(username+" with role default have an exemption , the user has write access to device "+device_id)
                            device_updated_details = self._db.update_single_data(DeviceModel.DEVICE_COLLECTION,id,field,field_value)
                            return device_updated_details
                        
                    print(username+" don't have write access in Device DB")
            else:
                self._latest_error = f'User id {username} is invalid'
                return -1
            
             
# Weather data document contains device_id (String), value (Integer), and timestamp (Date) fields
class WeatherDataModel:
    WEATHER_DATA_COLLECTION = 'weather_data'

    def __init__(self):
        self._db = Database()
        self._latest_error = ''
    
    # Latest error is used to store the error string in case an issue. It's reset at the beginning of a new function call
    @property
    def latest_error(self):
        return self._latest_error
    
    # Since device id and timestamp should be unique in weather_data collection, this provides a way to fetch the data document based on the device id and timestamp
    def find_by_device_id_and_timestamp(self, device_id, timestamp):
        key = {'device_id': device_id, 'timestamp': timestamp}
        return self.__find(key)
    
    # Finds a document based on the unique auto-generated MongoDB object id 
    def find_by_object_id(self, obj_id):
        key = {'_id': ObjectId(obj_id)}
        return self.__find(key)
    
    # Private function (starting with __) to be used as the base for all find functions
    def __find(self, key):
        wdata_document = self._db.get_single_data(WeatherDataModel.WEATHER_DATA_COLLECTION, key)
        return wdata_document
    
    # This first checks if a data item already exists at a particular timestamp for a device id. If it does, it populates latest_error and returns -1.
    # If it doesn't already exist, it'll insert a new document and return the same to the caller
    def insert(self, device_id, value, timestamp, username):
        self._latest_error = ''
        wdata_document = self.find_by_device_id_and_timestamp(device_id, timestamp)
        if (wdata_document):
            self._latest_error = f'Data for timestamp {timestamp} for device id {device_id} already exists'
            return -1
        Userdetails = UserModel()
        Userdtls = Userdetails.find_by_username(username)
           
        if (Userdtls['role'] == "admin"):
            weather_data = {'device_id': device_id, 'value': value, 'timestamp': timestamp}
            wdata_obj_id = self._db.insert_single_data(WeatherDataModel.WEATHER_DATA_COLLECTION, weather_data)
            return self.find_by_object_id(wdata_obj_id)
        else:
            device_exception = Userdtls['device_exception']
            devices=device_exception.split("_")
            for i in devices:
                if(i==device_id):
                   print(username+" with role default have an exemption , the user has write\modify access to weather details for device "+device_id)
                   weather_data = {'device_id': device_id, 'value': value, 'timestamp': timestamp}
                   wdata_obj_id = self._db.insert_single_data(WeatherDataModel.WEATHER_DATA_COLLECTION, weather_data)
                   return self.find_by_object_id(wdata_obj_id)
            print(username+" dont have write access in WeatherDB")


#pdate the weather details
    def update(self, device_id,db_timestamp,field, field_value, username):
        self._latest_error = ''
        devicedetails = DeviceModel()
        ddata_document = devicedetails.find_by_device_id(device_id)
        if (ddata_document):
            Userdetails = UserModel()
            Userdtls = Userdetails.find_by_username(username)
            if (Userdtls['role'] == "admin"):
                #db_timestamp = ddata_document['timestamp']
                document = self.find_by_device_id_and_timestamp(device_id,db_timestamp)
                id = document['_id']
                if(document):
                    print(field + field_value)
                    if((field == 'timestamp') and (field_value == db_timestamp)):
                        self._latest_error = f'Data for timestamp {db_timestamp} for device id {device_id} already exists'
                        return -1
                    else:
                        device_updated_details = self._db.update_single_data(WeatherDataModel.WEATHER_DATA_COLLECTION,id,field,field_value)
                        return device_updated_details
            else: 
                device_exception = Userdtls['device_exception']
                devices=device_exception.split("_")
                for i in devices:
                    if(i==device_id):
                        
                        print(username+" with role default have an exemption , the user has write\modify access to weather details for device "+device_id)
                      #  db_timestamp = ddata_document['timestamp']
                        document = self.find_by_device_id_and_timestamp(device_id,db_timestamp)
                        id = document['_id']
                        print(id)
                        if(document):
                            
                            if((field =='timestamp') and (field_value == db_timestamp)):
                                self._latest_error = f'Data for timestamp {db_timestamp} for device id {device_id} already exists'
                                return -1
                            else:
                                weather_updated_details = self._db.update_single_data(WeatherDataModel.WEATHER_DATA_COLLECTION,id,field,field_value)
                                print(weather_updated_details)
                                return weather_updated_details
                print(username+" don't have write access in Device DB")


# DailyReportModel data document contains device_id (String), value (Integer), and timestamp (Date) fields
class DailyReportModel:
    DAILY_REPORT_COLLECTION = 'daily_reports'
    def __init__(self):
        self._db = Database()
        self._latest_error = ''
    
    # Latest error is used to store the error string in case an issue. It's reset at the beginning of a new function call
    @property
    def latest_error(self):
        return self._latest_error
    
    # Since device id and day should be unique in daily_report collection, this provides a way to fetch the data document based on the device id and timestamp
    def find_by_device_id_and_day(self, device_id, day):
        key = {'_id.device_id': device_id, '_id.day': day}
        return self.__find(key)
    
    # Finds a document based on the unique auto-generated MongoDB object id 
    def find_by_object_id(self, obj_id):
        key = {'_id': ObjectId(obj_id)}
        return self.__find(key)
    
    # Private function (starting with __) to be used as the base for all find functions
    def __find(self, key):
        daily_report_document = self._db.get_single_data(DailyReportModel.DAILY_REPORT_COLLECTION, key)
        return daily_report_document
    def __findall(self, key):
        daily_report_document = self._db.get_all_data(DailyReportModel.DAILY_REPORT_COLLECTION, key)
        return daily_report_document

    #fetch detail daily_report collection using below query
    #{   $and:[{"_id.day":{$gt:1}},{"_id.day":{$lt:4}},{"_id.device_id":'DH001'}]}
  
    def fetchData(self,stDay,endDay,device_id):
        dailyreportdtls = DailyReportModel()
        
        searchquery=[{"$match": {"$expr":{ "$and": [{ "$gte": [ "$_id.day", stDay ]},{ "$lte": [ "$_id.day", endDay ] },{"$eq":["$_id.device_id",device_id]}]}}},{"$group": {'_id':'null' }}]
        dailyreport_documents = dailyreportdtls.__findall(searchquery)
        #text = dailyreport_documents
        #jsondata = text["result"]
        
      
        return dailyreport_documents