

import itertools 
DELIVERY_MAP_CONFIG = 'M01-W01-04-Project-Assessment-Nile-Mart/M01-W01-04-Project-Assessment-Nile-Mart/v2/config/delivery_map.txt'
ORDER_BATCH_CONFIG = 'M01-W01-04-Project-Assessment-Nile-Mart/M01-W01-04-Project-Assessment-Nile-Mart/v2/config/order_batch.txt'

#Class Order ​stores details of an individual order, and triggers delivery via a route  
class Order:
    def __init__(self, id, item_name, customer, order_date, city, delivery_date, delivery_type):
        self._id = id
        self._item_name = item_name
        self._customer = customer
        self._order_date = order_date
        self._city = city
        self._delivery_date = delivery_date
        self._delivery_type = delivery_type

    def __str__(self):
        return f'ID - {self.id}, Item Name - {self.item_name}, Order Date - {self.order_date}, Customer - {self.customer}, City - {self.city}, Delivery Date - {self.delivery_date}, Delivery Type - {self.delivery_type}'

    @property
    def id(self):
        return self._id

    @property
    def item_name(self):
        return self._item_name

    @property
    def order_date(self):
        return self._order_date

    @property
    def customer(self):
        return self._customer

    @property
    def city(self):
        return self._city

    @property
    def delivery_date(self):
        return self._delivery_date

    #defining delivery_type
    @property
    def delivery_type(self):
        return self._delivery_type

    #Printing Dispatching order details   
    def dispatch(self, delivery_route):
        print(f'=============================================================================================================================================================================')
        print(f'Dispatching order {order}')
        print(f'=============================================================================================================================================================================')

        delivery_route.process_order(self)

#Class OrderBatch ​parses order information from ​order_batch.txt​ and creates order objects
class OrderBatch:
    def __init__(self):
        self._order_batch = []

    def __str__(self):
        pass
    # Using read_config function: Read order_batch.txt file 
    # read each order details line by line , spilt the details of each order bases on'-' delimeter and store it in a list (order_details)
    # Calls order class and pass the order details.
    # Stores the order details in Order_batch List
    def read_config(self, order_batch_config):
        with open(order_batch_config, 'r') as obatch_file:
            obatch_lines = [obatch_line.rstrip() for obatch_line in obatch_file]

        for order_entry in obatch_lines:
            order_details = order_entry.split('-')
            order = Order(order_details[0], order_details[1], order_details[2], order_details[3], order_details[4], order_details[5], order_details[6])  

            self._order_batch.append(order)

    def get_orders(self):
        return self._order_batch
#Class DeliveryMap :  Reads delivery_map.txt file  and  fetch list of destination in the file and route map details
class DeliveryMap:
    def __init__(self):
        self._destinations = []
        self._delivery_map = {}
        self._delivery_type = []

    def __str__(self):
        pass
    # Using read_config function: Read delivery_map.txt file 
    # read each route details, spilt the details of each delivery reoute based on ' ' delimeter and store spilt result destination  and stages
    # Again we split stages based on ',' and get all reoute details or delivery stages
    # Store the details in a dictionary with Key as destination and value as stages
    # Print all destinations
    

    def read_config(self, delivery_map_config):
        with open(delivery_map_config, 'r') as dmap_file:
            dmap_lines = [dmap_line.rstrip() for dmap_line in dmap_file]

#Reoute details in delivery_map.txt 
        #Dria Premium Altar1-truck-Altar2,Altar2-flight-Dria
        #In the read config function  we will store each line of file in 2 list and a dictionary
        #Destination delivery_type  stages
        #Dria         Premium       Altar1-truck-Altar2,Altar2-flight-Dria
        for line in dmap_lines:
            destination,delivery_type,stages = line.split(" ",2)    
            #store destination details to list destination        
            self._destinations.append(destination)
            #store deivery tpe details to list delivery_type        
            self._delivery_type.append(delivery_type)
            #Splitng the stages details based "," delimeter and store it
            stages = stages.split(',')
            #delivery_map is a dict with key as destination and delivery_type and value as stages details
            self._delivery_map[destination,delivery_type] = stages
        #Printing list of destination 
        print(f'Destinations: {self._destinations}')

    #Getting destionation value
    def get_destinations(self):
        return self._destinations 

    #Getting delivery type
    def get_delivery_type(self):
        return self._delivery_type

    #getting route details using dict delivery_map
    def routing_map(self):
        return self._delivery_map

    #getting stages details based on destination and delivery_type
    def get_stages(self, delivery_center,delivery_type):
        return self._delivery_map[delivery_center,delivery_type]
    

# Class DeliveryStage :  Gives us details of delivery stage based on the source and destination
class DeliveryStage:
    def __init__(self, source, destination,dispatch_method):
        self._source = source
        self._destination = destination
        self._dispatch_method = dispatch_method
        self._next_stage = None

    @property
    def next_stage(self):
        return self._next_stage

    @next_stage.setter
    def next_stage(self, successor):
        self._next_stage = successor

    def process_order(self, order):
        pass


# Based on the source , destination and dispatch method we will print details of route
class Dispatch(DeliveryStage):
    def __init__(self, source, destination,dispatch_method):
        super().__init__(source, destination,dispatch_method)

    def __str__(self):
        return f'{self._dispatch_method} from {self._source} to {self._destination}'
    
    #Will print for an order train dispacth from source to destination
    def process_order(self, order):
        print(f'Order {order.id} - {self._dispatch_method} Dispatch from {self._source} to {self._destination}')

        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 

           
#DeliveryRoute ​class holds the structured route to a destination, with several stage

class DeliveryRoute:
    def __init__(self, stage_list, destination):
        self._stage_list = stage_list
        self._destination = destination
        
    #route details returned
    def __str__(self):
        route = ','.join(str(stage) for stage in self._stage_list)
        return f'Route to {self._destination} : {route}\n'
        

    def process_order(self, order):
        self._stage_list[0].process_order(order)

#DeliverySystem ​uses DeliveryMap to create usable routes to all destinations
class DeliverySystem:
    def __init__(self):
        self.delivery_centers = []
        self.stage_routes = {}
        self.delivery_type =[]
    #Pouplating route based on center and stages
    def populate_route(self, center, stages):
        stage_list = []
        #For each Stages, we will spilt based on '-' delimeter 
        # And store values in source,dispatch method and destination
        # First value contains source destination name second value contains dispatch method and third value contains final destination name
        for stage in stages:
            source, dispatch_method, destination = stage.split('-')
            stage_list.append(Dispatch(source, destination,dispatch_method.capitalize()))
        
        for i in range(0, len(stage_list) - 1):
            stage_list[i].next_stage = stage_list[i+1]
        
        #getting route details
        route = DeliveryRoute(stage_list, destination)
        print(route)

        return route
    # Creates and triggers DeliveryMap to ingest destination and stage information
    def configure(self, DELIVERY_MAP_CONFIG):
        delivery_map = DeliveryMap()
        delivery_map.read_config(DELIVERY_MAP_CONFIG)

        self.delivery_centers.extend(delivery_map.get_destinations())
        self.delivery_type.extend(delivery_map.get_delivery_type())
        #for each center and delivery_type ,we are getting route details
        for (center , delivery_type) in zip(self.delivery_centers , self.delivery_type):
            stages = delivery_map.get_stages(center,delivery_type)
            route = self.populate_route(center, stages)
            self.stage_routes[center,delivery_type] = route

    def get_route(self, destination,delivery_type):
            return self.stage_routes[destination,delivery_type]

        
# Client Context

delivery_system = DeliverySystem()
delivery_system.configure(DELIVERY_MAP_CONFIG)

order_batch = OrderBatch()
order_batch.read_config(ORDER_BATCH_CONFIG)

orders = order_batch.get_orders()
#For each order we will get route and print it
for order in orders:
    route = delivery_system.get_route(order.city,order.delivery_type)
    order.dispatch(route)
    print('\n')