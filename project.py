

class RentalUnit():

    
    insurance = 1481 # I looked and couldnt find a good value relating insurance value and property value - this fixed value causes higher priced things to have much higher ROI and 
    utilites = 0
    
    vacancy_rate =  (1 - .062)
    cc = .035
    Ptax = {
        "Hawaii": 0.28, 
        "Alabama": 0.41,
        "Colorado": 0.51,
        "Louisiana": 0.55,
        "District of Columbia": 0.56,
        "South Carolina": 0.57,
        "Delaware": 0.57,
        "West Virginia": 0.58,
        "Nevada": 0.6,
        "Wyoming": 0.61,
        "Arkansas": 0.62,
        "Utah": 0.63,
        "Arizona": 0.66,
        "Idaho": 0.69,
        "Tennessee": 0.71,
        "California": 0.76,
        "New Mexico": 0.8,
        "Mississippi": 0.81,
        "Virginia": 0.82,
        "Montana": 0.84,
        "North Carolina": 0.84,
        "Indiana": 0.85,
        "Kentucky": 0.86,
        "Florida": 0.89,
        "Oklahoma": 0.9,
        "Georgia": 0.92,
        "Missouri": 0.97,
        "Oregon": 0.97,
        "North Dakota": 0.98,
        "Washington": 0.98,
        "Maryland": 1.09,
        "Minnesota": 1.12,
        "Alaska": 1.19,
        "Massachusetts": 1.23,
        "South Dakota": 1.31,
        "Maine": 1.36,
        "Kansas": 1.41,
        "Michigan": 1.54,
        "Ohio": 1.56,
        "Iowa": 1.57,
        "Pennsylvania": 1.58,
        "Rhode Island": 1.63,
        "New York": 1.72,
        "Nebraska": 1.73,
        "Texas": 1.80,
        "Wisconsin": 1.85,
        "Vermont": 1.9,
        "Connecticut": 2.14,
        "New Hampshire": 2.18,
        "Illinois": 2.27,
        "New Jersey": 2.49,
    }




    def __init__(self, State, Value, Time, Interest, Renovations = 0):
        self.state = State
        self.value = Value # Value that is fixed at the start
        self.Time = Time # Years
        self.month = self.Time * 12 # Convert Monthly expenses to Yearly 
        self.renovations = Renovations
        self.interest = Interest/((100*12))
        self.downpayment = Value * (1/5)
        self.mortgage = Value * (4/5)
        self.currentv = self.value # Value that will change over time
        self.closingcosts = RentalUnit.cc * Value
        self.HOA = 100
        self.propertytax = RentalUnit.Ptax[State] / 100
        self.marketingcost = .075 * Value
        self.insurance = (Value / 2000) * self.month # Guesstimate based on video we received, all looked up value way too high to make sense


    def rent(self): #Per Year
        return (self.Averagev() * .01 * RentalUnit.vacancy_rate * self.month)

    def numbergoup(self): #Per Year
        self.currentv = self.value ** (1.03)^self.Time

    def mortgagepayment(self): # Per month - 
        return (self.mortgage * (self.interest * (self.interest*((1 + self.interest)**360)))) / ((1 + self.interest)**(359))
        #(P * r(1 + r)**n) / (1 + r)**(n-1)

    def Mantinace(self): #Per Year - Recommended value to save is 50% of rent
        return self.rent() * (1/2)

    def Averagev(self): # used for calculaing rent - calcs the average propertiy value over the course of the investment
        alist = [self.value]
        if self.Time == 1:
            return self.value
        else:
            for i in range(2, self.Time+1):
                alist.append(self.value * (1.035**i))
            return sum(alist) / len(alist)
    
    def ClosingCosts(self): #One Time
        return self.value * RentalUnit.cc 
    
    def investment(self): #One Time
        return self.downpayment + self.closingcosts + self.renovations 
    
    def costs(self): #Per Year
        return (self.mortgagepayment() * self.month) + (self.propertytax * self.Averagev() * self.Time) + self.Mantinace() + (self.HOA * self.month) + (self.insurance) + (RentalUnit.utilites * self.month)

    def income(self): #Per Year
        return self.rent()

    def cashflow(self): #Per Year
        return self.income() - self.costs()
    def cashoncashROI(self):
        return (self.cashflow() / self.investment()) * 100

    def decToPercent(decimal):
        return f"{decimal * 100}%"



def run():
    
    
    while True:
        a = input('What state do you live in? :')
        if a not in RentalUnit.Ptax:
             print(f'Invalid state name please try again :')
        else: 
                break

    while True: 
        b = input('What is the value of the property you are purchasing :')
        if b.isdigit() == True:
            break
        else:
            print( f'Please enter a valid amount ')
        
    while True: 
        c = input('Over what how many years are you looking to calculate your return on investment :')
        if c.isdigit() == True:
            break
        else:
            print( f'Please enter a valid amount ')

    while True: 
        d = input('What is the interest rate on you mortgage :')
        if d.isdigit() == True:
            break
        else:
            print( f'Please enter a valid amount ')

    while True: 
        e = input('How much did you spend on renovations? :')
        if e.isdigit() == True:
            break
        else:
            print( f'Please enter a valid amount ')



    
    Myhouse = RentalUnit(a,int(b),int(c),float(d),int(e))
    print(f' Your return on your initial investment {Myhouse.cashoncashROI()} %')
    



run()






#Myhouse = RentalUnit('Florida', 250000, 2, 3)

#print(Myhouse.cashoncashROI())
#print(Myhouse.Averagev())