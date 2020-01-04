class Vehicle(object):
    def __init__(self, name="",modelyear=0000,miles=0, VINum=0 ):
        self.vname=name
        self.modyr = modelyear
        self.mile=miles
        self.vins = VINum
    def __str__(self):
        return self.vname+ "" + self.modyr + "" + self.mile+""+self.vins
    def __repr__(self):
        return self.__str__()

class Boat(Vehicle):
    def __init__(self,name='', modelyear=0, miles=0, VINum=0, nowheels=True,floats=True):
        self.nowheels= nowheels
        self.floats=floats
        Vehicle.__init__(name=name, modelyear=modelyear, miles=miles, VINum=VINum)

    def __str__(self):
        return self.vname + self.modyr+self.mile+self.vins+ "this vehicle has no wheels" +str(self.nowheels) + "this vehicle is on land "
        +str(floats)

class Wheeled(Vehicle):
    def __init__(self, name='', modelyear=0, miles=0, VINum=0,handles=False,numwheels=0,):
        Vehicle.__init__(name=name, modelyear=modelyear, miles=miles, VINum=VINum)
        self.handles=handles
        self.numwheels=numwheels
    def __str__(self):
        return self.vname + self.modyr+self.mile+self.vins+ "this vehicle has handles" +str(self.handles) + "this vehicle has this many wheels "
        +str(self.numwheels)

class Bicycle(Wheeled):
    def __init__(self, name='', modelyear=0, miles=0, VINum=0, handles=False, numwheels=0, twowheels=True, pedals=True):
        super().__init__(name=name, modelyear=modelyear, miles=miles, VINum=VINum, handles=handles, numwheels=numwheels)
        self.twowheels=twowheels
        self.pedals=pedals
    def __str__(self):
        return self.vname + self.modyr+self.mile+self.vins+ "this vehicle has two wheels" +str(self.twowheels) + "this vehicle has pedals "
        +str(self.pedals)
class Car(Wheeled):
    def __init__(self, name='', modelyear=0, miles=0, VINum=0, handles=False, numwheels=0, numdoor=0,numofpassengers=0):
        super().__init__(name=name, modelyear=modelyear, miles=miles, VINum=VINum, handles=handles, numwheels=numwheels)
        self.numdoor.numdoor
        self.numofpassengers=numofpassengers
    def __str__(self):
        return self.vname + self.modyr+self.mile+self.vins+ "handles?:" +self.handles + "number of wheels" + self.numwheels + "number of doors"
        +self.numdoor + "number of passengers: "+self.numofpassengers
class TwoDoor(Car):
    def __init__(self, name='', modelyear=0, miles=0, VINum=0, handles=False, numwheels=0, numdoor=0, numofpassengers=0, backseat=False, sportscar=True ):
        super().__init__(name=name, modelyear=modelyear, miles=miles, VINum=VINum, handles=handles, numwheels=numwheels
        ,numdoor=numdoor, numofpassengers=numofpassengers)
        self.backseat=backseat
        self.sportscar=sportscar
    def __str__(self):
        return self.vname + self.modyr+self.mile+self.vins+ "handles?:" +self.handles + "number of wheels" + self.numwheels + "number of doors"
        +self.numdoor + "number of passengers: "+self.numofpassengers + "this car has a backseat" + self.backseat + "this car is a sports car" + self.sportscar
class FourDoor(Car):
    def __init__(self, name='', modelyear=0, miles=0, VINum=0, handles=False, numwheels=0, numdoor=0, numofpassengers=0, minivan=False, highmileage = True):
        super().__init__(name=name, modelyear=modelyear, miles=miles, VINum=VINum, handles=handles, numwheels=numwheels, numdoor=numdoor, numofpassengers=numofpassengers)
        self.minivan=minivan
        self.highmileage=highmileage
    def __str__(self):
        return self.vname + self.modyr+self.mile+self.vins+ "handles?:" +self.handles + "number of wheels" + self.numwheels + "number of doors"
        +self.numdoor + "number of passengers: "+self.numofpassengers + "this car is a minivan" + self.minivan + "this car has high mileage" + self.highmileage