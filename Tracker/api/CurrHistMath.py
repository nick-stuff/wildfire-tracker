#Imports from Python libraries
import pandas as pd #Used to read in the csv files
import numpy as np #Used in case of an array
import matplotlib.pyplot as plt #Used to plot our data, in this case as a bar graph or pie chart
import math as math #Used for some of the math that is involved (count, range, etc)


#Class for the backend of the Comparison section of the app
class CurrHistMath:

    #Setting up global variables
    numOfCurrentFires = 0 #Initializing the number of current fires
    numOfHistoricalFires = 0 #Initializing the number of historical fires
    startLocation = "" #Taking the user inputted start location as a string; this information needs to be called from the initial login / question
    
    #Test values for long and lat
    long = -120.000000 #initializing the longitude for the coordinates from User Inputted location, will change, current value is for testing
    lat = 55.000000 #initializing the latitude for the coordinates from User Inputted location, will change, current value is for testing

    #All things that are committed currently are tested and working locally as intended
    #@staticmethod
    def set_user_longlat(userLt, userLng):
        CurrHistMath.long = userLng
        CurrHistMath.lat = userLt
        #this should change the values so we can update everything according to user location
        #debug msg
        



    #Getting the current number of fires
    def current_num_fires():
        #print(str(lat) + "     " + str(long),flush=True)
        #Setting up variables and constants
        #1 degree of change in Latitude is 111.1 km, so for a squared area with length 111.1km we need half a degree
        latDegreeAdjust = 0.500000 #The amount of distance from the intial point we're counting from
        longDegreeAdjust = 0.500000 #The amount of distance from the inital point we're counting from
    
        userLong = CurrHistMath.long #Setting the user inputted location longitude
        userLat = CurrHistMath.lat #Setting the user inputted location latitude
    
        #Setting the range values
        latLow = userLat - latDegreeAdjust #Getting the southern based range
        latHigh = userLat + latDegreeAdjust #Getting the northern based range

        longLow = userLong - longDegreeAdjust #Getting the western based range
        longHigh = userLong + longDegreeAdjust #Getting the eastern based range

        #Calling the data file for the currently active fires
        currentFires = pd.read_csv('C_FIRE_PNT.csv') #File name for current / on-going fires
    
        #Getting the columns of Longitude and Latitude based on the area (values of long and lat in the rows)
        currentFires = currentFires[['LATITUDE', 'LONGITUDE']] 
        #print(currentFires.columns.tolist())
        #print(currentFires['LATITUDE'])
        #print(currentFires['LONGITUDE'])

        #Getting the specific rows based on the area of the fires
        currentFiresLat = currentFires['LATITUDE'].between(latLow, latHigh)
        #print("After first between")
        #print(currentFires[currentFiresLat])
    
        currentFires = currentFires[currentFiresLat]
        #print("This is after the first between and merge")
        #print(currentFires)
    
        currentFiresLong = currentFires['LONGITUDE'].between(longLow, longHigh)
        #print("After second between")
        #print(currentFires)
      
        currentFires = currentFires[currentFiresLong]
        #print("This is after the second between and merge")
        #print(currentFires)
    
        numOfCurrentFires = len(currentFires) #Getting the number of current fires
   
        return numOfCurrentFires 

    #Getting the historical number of fires for the region
    def historical_num_fire():
        #Setting up variables and constants
        #1 degree of change in Latitude is 111.1 km, so for a squared area with length 111.1km we need half a degree
        latDegreeAdjust = 0.500000 #The amount of distance from the intial point we're counting from
        longDegreeAdjust = 0.500000 #The amount of distance from the inital point we're counting from
    
        userLong = CurrHistMath.long #Setting the user inputted location longitude
        userLat = CurrHistMath.lat #Setting the user inputted location latitude
        print(str(userLong) + "     " + str(userLat),flush=True)
    
        #Setting the range values
        latLow = userLat - latDegreeAdjust #Getting the southern based range
        latHigh = userLat + latDegreeAdjust #Getting the northern based range

        longLow = userLong - longDegreeAdjust #Getting the western based range
        longHigh = userLong + longDegreeAdjust #Getting the eastern based range
    
        #Calling the data file for the historical fires
        historicalFires = pd.read_csv('BC_Fire_Point_2022.csv') #This file name will be changed later
        #print(historicalFires.columns.tolist())

        #Getting the columns of Longitude and Latitude based on the area (values of long and lat in the rows)
    
        historicalFires = historicalFires[['LATITUDE', 'LONGITUDE']]    
        #print(historicalFires)
        #print(historicalFires.columns.tolist())
        #print(historicalFires['LATITUDE'])
        #print(historicalFires['LONGITUDE'])
    
        #Getting the specific rows based on the area of the fires
        historicalFiresLat = historicalFires['LATITUDE'].between(latLow, latHigh)
        #print("After first between")
        #print(historicalFires[historicalFiresLat])
    
        historicalFires = historicalFires[historicalFiresLat]
        #print("This is after the first between and merge")
        #print(historicalFires)
    
        historicalFiresLong = historicalFires['LONGITUDE'].between(longLow, longHigh)
        #print("After second between")
        #print(currentFires)
      
        historicalFires = historicalFires[historicalFiresLong]
        #print("This is after the second between and merge")
        #print(currentFires)
   
        numOfHistoricalFires = len(historicalFires) #Getting the number of current fires

        return numOfHistoricalFires

    #Comparing the current and historical fire data, printing / displaying if the current fires are an increase or decrease of previous fires
    def compare_fire():
        #Comparing the number of fires based on the previous two functions
        numCurrentFires = CurrHistMath.current_num_fires()
        numHistoricalFires = CurrHistMath.historical_num_fire()
        message = ""
    
        if (numHistoricalFires < numCurrentFires):
            message = "There has been an increase in fire activity since last year" #These may change from print statements to something else based on framework; display?
        elif (numHistoricalFires > numCurrentFires):
           message = "There has been a decrease in fire activity since last year" #These may change from print statements to something else based on framework; display?
        else:
           message = "The amount of fire activity is the same" #These may change from print statements to something else based on framework; display?
        
        return message 
    
   
    #Function to display the current number of fires
    def current_num_message():
        
        numCurrentFires = CurrHistMath.current_num_fires() #Historical number of fires
        stringCurrentNum = str(numCurrentFires)
        currentMessage = "The on-going number of fires for the region is: " + stringCurrentNum
        
        return currentMessage
    
    #Function to display the historical number of fires
    
    def historical_num_message():
        numHistoricalFires = CurrHistMath.historical_num_fire() #Current number of fires

        stringHistoricalNum = str(numHistoricalFires)
        historitcalMessage = "The historical number of fires for the region is: " + stringHistoricalNum
        
       
       
        return historitcalMessage 

    #Showing the piechart for the percentange
    def display_graph():
        numHistoricalFires = CurrHistMath.historical_num_fire() #Current number of fires
        numCurrentFires = CurrHistMath.current_num_fires() #Historical number of fires

        percentTotal = numHistoricalFires + numCurrentFires #Total number of fires for historical and current

        percentOfCurrent = round((numCurrentFires / percentTotal) * 100, 0) #Percentage of current fires compared to historical and current
        percentOfFires = round((numHistoricalFires / percentTotal) * 100, 0) #Percentage of historical fires compared to historical and current

        stringOfCurrent = str(percentOfCurrent)
        stringOfHistorical = str(percentOfFires)
    
        percentArray = np.array([percentOfCurrent, percentOfFires])
        labels = ["Current Fires: \n" + stringOfCurrent + "%", "Historical Fires: \n" + stringOfHistorical + "%"]
        #Might need to change this for the Flask file, might need to change it to Figure
        #chart = plt.pie(percentArray, labels = labels)
        #Need to use plt here to show the pie chart
        #chartShow = plt.show()
        sizes = [percentOfCurrent, percentOfFires]
        explode = (0.1, 0)  # explode the 1st slice (current fires)

        fig, ax = plt.subplots()  # Create a new figure and axis
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140,labeldistance=1.2 )
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        return fig

    #Function to display the historical fires on the map   
    def firesInArea_test(lt,lng):
        #Setting up variables and constants
        #1 degree of change in Latitude is 111.1 km, so for a squared area with length 111.1km we need half a degree
        latDegreeAdjust = 0.500000 #The amount of distance from the intial point we're counting from
        longDegreeAdjust = 0.500000 #The amount of distance from the inital point we're counting from
    
        userLong = lng #Setting the user inputted location longitude
        userLat = lt #Setting the user inputted location latitude
    
        #Setting the range values
        latLow = userLat - latDegreeAdjust #Getting the southern based range
        latHigh = userLat + latDegreeAdjust #Getting the northern based range

        longLow = userLong - longDegreeAdjust #Getting the western based range
        longHigh = userLong + longDegreeAdjust #Getting the eastern based range
    
        #Calling the data file for the historical fires
        currentFires = pd.read_csv('C_FIRE_PNT.csv') #This file name will be changed later (Move to /datasets/name)?
    
        #Getting the columns of Longitude and Latitude based on the area (values of long and lat in the rows)
        currentFires = currentFires[['LATITUDE', 'LONGITUDE', 'GEO_DESC', 'FIRE_YEAR']] 
        #print(currentFires.columns.tolist())
        #print(currentFires['LATITUDE'])
        #print(currentFires['LONGITUDE'])

        #Getting the specific rows based on the area of the fires
        currentFiresLat = currentFires['LATITUDE'].between(latLow, latHigh)
        #print("After first between")
        #print(currentFires[currentFiresLat])
    
        currentFires = currentFires[currentFiresLat]
        #print("This is after the first between and merge")
        #print(currentFires)
    
        currentFiresLong = currentFires['LONGITUDE'].between(longLow, longHigh)
        #print("After second between")
        #print(currentFires)
      
        currentFires = currentFires[currentFiresLong]
        #print("This is after the second between and merge")
        #print(currentFires)
    
        numOfCurrentFires = len(currentFires) #Getting the number of current fires
        #print("This is after the second between and merge")
        #print(currentFires)
        
        #print(currentFires,flush=True)
        jsonString = currentFires.to_json(orient='records')

    

        return jsonString
    
    #Function to display the current fires on the map 
    def historicalfiresInArea_test(lt,lng):
        #Setting up variables and constants
        #1 degree of change in Latitude is 111.1 km, so for a squared area with length 111.1km we need half a degree
        latDegreeAdjust = 0.500000 #The amount of distance from the intial point we're counting from
        longDegreeAdjust = 0.500000 #The amount of distance from the inital point we're counting from
    
        userLong = lng #Setting the user inputted location longitude
        userLat = lt #Setting the user inputted location latitude
    
        #Setting the range values
        latLow = userLat - latDegreeAdjust #Getting the southern based range
        latHigh = userLat + latDegreeAdjust #Getting the northern based range

        longLow = userLong - longDegreeAdjust #Getting the western based range
        longHigh = userLong + longDegreeAdjust #Getting the eastern based range
    
        #Calling the data file for the historical fires
        historicalFires = pd.read_csv('BC_Fire_Point_2022.csv') #This file name will be changed later
        #print(historicalFires.columns.tolist())

        #Getting the columns of Longitude and Latitude based on the area (values of long and lat in the rows)
    
        historicalFires = historicalFires[['LATITUDE', 'LONGITUDE', 'Name', 'IGNITION_DATE']]    
        #print(historicalFires)
        #print(historicalFires.columns.tolist())
        #print(historicalFires['LATITUDE'])
        #print(historicalFires['LONGITUDE'])
    
        #Getting the specific rows based on the area of the fires
        historicalFiresLat = historicalFires['LATITUDE'].between(latLow, latHigh)
        #print("After first between")
        #print(historicalFires[historicalFiresLat])
    
        historicalFires = historicalFires[historicalFiresLat]
        #print("This is after the first between and merge")
        #print(historicalFires)
    
        historicalFiresLong = historicalFires['LONGITUDE'].between(longLow, longHigh)
        #print("After second between")
        #print(currentFires)
      
        historicalFires = historicalFires[historicalFiresLong]
        #print("This is after the second between and merge")
        #print(currentFires)
   
        numOfHistoricalFires = len(historicalFires) #Getting the number of current fires
        
        #print(historicalFires,flush=True)
        jsonString = historicalFires.to_json(orient='records')

    

        return jsonString