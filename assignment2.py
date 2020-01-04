#miles and km
class Odometer(object):
    def __init__(self,miles=5, kil=8.04672):
        self.mi=miles
        self.km=kil
        try:        #checking to see if it is an int
            int(self.mi)
        except:
            try:    #checking to see if it is a float
                float(self.mi)
            except:     #if not assign to default value
                print("this input is not a number:", self.mi)
                self.mi = 5
        try:        #checking to see if it is an int
            int(self.km)
        except:
            try:      #checking to see if it is a float
                float(self.km)
            except:
                print("this input is not a number:", self.km)
                self.km = 8.04672
        if(self.mi <0):     #checking for negative values
            print("You can't have a negative mi: ",self.mi )
            self.mi = 5
        if(self.km<0):      #checking for negative values
            print("You can't have a negative km: ", self.km)
            self.km=8.04672

    def __str__(self):
        return "miles: "+str(self.mi)+" kilometers: "+str(self.km)+"\n"
        

    def __repr__(self):
        return self.__str__()

    def __add__(self, odometer):
        result = self.mi + odometer.mi
        result2= self.km +odometer.km
        return "total miles:" + str(round(result,1)), "total km:" + str(round(result2,1))   #rounding to 1/10 of mile/km

    def __sub__(self, odometer):
        result = self.mi - odometer.mi
        result2 = self.km - odometer.km
        if (result < 0):        #shouldn't be a negative value
            result =0
        if (result2 <0):
            result2 = 0
        return "the subtracted miles is: "+ str(round(result,1)), " the subtracted km is: " + str(round(result2,1))


myO1 = Odometer(10)
myO2 = Odometer(20,2.4)
myO3 = Odometer(-10,-20.5)
myO4= Odometer("p",  "k")
print(myO1,myO2,myO3,myO4)
y= myO1.__add__(myO2)
x=myO1.__sub__(myO2)
print(myO3.__repr__())
print(myO4.__str__())
print(y)
print(x)


""" OUTPUT
miles: 10 kilometers: 8.04672
 miles: 20 kilometers: 2.4
 You can't have a negative mi

You can't have a negative km

miles: 5 kilometers: 8.04672
 this input is not a number: p
this input is not a number: k
miles: 5 kilometers: 8.04672

miles: 5 kilometers: 8.04672

miles: 5 kilometers: 8.04672

('total miles:30', 'total km:10.4')
('the subtracted miles is: 0', ' the subtracted km is: 5.6')
"""