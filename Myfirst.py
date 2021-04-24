# print ("My first python program in github")

# Python program to illustrate the use of
# @property decorator
  
# Creating class
class Celsius:
      
    # Defining init method with its parameter
    def __init__(self, temp = 0):
        self._temperature = temp
  
    # @property decorator
    @property
      
    # Getter method
    def temp(self):
          
        # Prints the assigned temperature value
        print("The value of the temperature is: ")
        return self._temperature
  
    # Setter method
    @temp.setter
    def temp(self, val):
          
        # If temperature is less than -273 than a value
        # error is thrown
        if val < -273:
            raise ValueError("It is a value error.")
          
        # Prints this if the value of the temperature is set
        print("The value of the tempereture is set.")
        self._temperature = val
  
  
# Creating object for the stated class 
cel = Celsius();
  
# Setting the temperature value
cel.temp = -270
  
# Prints the temperature that is set
print(cel.temp)
  
# Setting the temperature value to -300
# which is not possible so, an error is 
# thrown
cel.temp = -300