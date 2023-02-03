import random

#emergency system (fire extinguishing, backup generators to hook into the power system)
#power system

class mainframe:
    def __init__(self):
        #setting up individual room costs (per night)
        self.roomHierarchyClass={"Economy":50,"Economy Plus":100,"Suite":200}
        #security deposit room prices
        self.roomSecurityDeposit = {'Economy':25,'Economy Plus':50,'Suite':100}
        #create a reservation list dictionary to store a one-to-one relationship between client and the room they are given at the time the reservation is made
        self.reservationList={}

    def getReservationList(self):
        return self.reservationList

    def createDbMainframe():
        frame=[]
        rooms=[]

    #c variable is a client object
    def makePayment(self,total,room):
        #add a charge for credit card transactions
        r=Room
        c=Client
        if room not in self.reservationList and room not in r.roomsOccupied:
            r.roomCost=(self.roomHierarchyClass[room]-10)+r.roomQuality
        creditFee=1.05
        subTotal=r.roomCost+self.roomSecurityDeposit
        totalCost=subTotal*creditFee
        c.amountpayed=totalCost
        print(f"Your total cost for this experience comes up to ${totalCost}")

    def checkInClients(self):
        c=Client
        print("Please input your name using the pull-out keyboard on the kiosk: (First, Middle, Last)")
        clientName=input()
        c.name=clientName.split(", ")
        print(f"Hello {c.name[0]} {c.name[2]}. Please input the most convenient forms of contact: (separate with commas)")
        clientContact=str(input())
        c.contactInformation=clientContact.split(", ")
        print("If you have any dietary restrictions (i.e. allergies), please input them below:")
        clientDiet=input()
        c.dietaryRestrictions=clientDiet.split(", ")

    def welcomeScreen(self):
        print("Hello customer, welcome to The Grand Quandale Hotel!")
        print("Are you making a reservation online or checking in at one of our locations?")
        inputChoice=input()
        if "check" in inputChoice.lower():
            mainframe.checkInClients(mainframe)
        elif "reserv" in inputChoice.lower():
            Client.takeReservation()

class Room(mainframe):
    def __init__(self):
        #integer values
        self.roomNumber=0
        self.floorCount = 3
        self.roomCapacity = 4
        self.roomQuality = 10
        #depending on quality of room (out of 10)
        #combination of quality (which floor and features)
        #subtract values from original quality score
        self.roomCost=0

        #True=room is open
        #False=room is occupied
        self.roomAvailability=True
        self.roomsOccupied=[]
        self.reservationList={}

    def determineRoomCost(self,room,reservationList):
        #score can be determined also by how person checking out left it
        mf=mainframe
        if room not in reservationList and room not in self.roomsOccupied:
            self.roomCost=(mf.roomHierarchyClass[room]-10)+self.roomQuality
            print(f"your room will cost {self.roomCost}")

    def determineRoomQuality(self):
        #allows the client to choose level/floor of room
        mf=mainframe
        print("Thank you for registering with us! Please select which type of room you would like:")
        print(mf.roomHierarchyClass)
        room=input()
        return room

    def airConditioner(self,temp):
        if temp >= 72:
            print("Would you like to turn the room temperature down to a normal 68 degrees?")
            tempControl = input()
            if tempControl == "Yes":
                temp = 68
            elif tempControl == "No":
                temp = temp
        elif temp <= 64:
            print("Would you like to turn the room temperature up to a normal 68 degrees?")
            tempControl = input()
            if tempControl == "Yes":
                temp = 68
            elif tempControl == "No":
                temp = temp
        else:
            temp = temp

    def foodService(self,owedMoney):
        print("Are you hungry? We have some delicacies from the local Dougmart")
        hungryOrNah = input()
        if hungryOrNah == "Yes":
            print("Welcome to Flavor Town, population you")
            print("We got chimken broth, frog legs, pickled soup, aged salmon, and mints stolen from another restaurant")
            print("What would you like to order?")
            daGrub = input()
            if daGrub == "Chimkin broth":
                print("That'll be $10")
                owedMoney = 10*1.08
            elif daGrub == "Frog legs":
                print("That will be $20")
                owedMoney = 20*1.08
            elif daGrub == "pickled soup":
                print("That'll be $15")
                owedMoney = 15*1.08
            elif daGrub == "Aged salmon":
                print("Thatll be $40")
                owedMoney = 40*1.08
            elif daGrub == "Mints":
                print("Thatll be $5")
                owedMoney = 5*1.08
            
    
    def cleaningService(self,room,lemonPledge):
        if room == "Dirty":
            print("Hola. Soy aqui limpio su habitacion, heuele a mierda de elphante")
            if lemonPledge == "Present":
                room = "Clean"
            else:
                room = "Dirty"
                print("Necesito más producto de limpieza de limón")
        else:
            room = "Clean"

    def fireSupression(self):
        if hotelStatus=="fine":
            fireSupressionSystem="Inactive"
        elif hotelStatus=="Not good":
            fireSupressionSystem="Acitve"

class Client(mainframe):
    def __init__(self):
        #string values
        self.name=[]
        #integer value
        self.assignedRoom=0
        #list value
        self.contactInformation=[]
        
        #$50 low tier, $100 mid tier, $200 high tier
        self.securityDeposit=0
        self.checkOutPayment=0
        self.hotelGiftBalance=0

        #list of strings ['seafood', 'nut']
        self.dietaryRestrictions=None
        self.timeOfCheckIn=None
        self.clientstatus="Respectable"
        #string value
        self.formOfPayment=[]

        #float value
        self.amountpayed=0.0


    def accessReservationList(self):
        mf=mainframe
        reservations=mf.getReservationList
        return reservations



    #c is a client parameter and r is a room parameter
    def checkIfOccupied(self,room,roomsOccupied):
        
        if room in roomsOccupied:
            return True
        elif room in Client.accessReservationList():
            return True
        else:
            return False


    def setRoomNumber(self, number, roomsOccupied):
        while True:
            r=Room
            if self.amountpayed <=50:
                self.assignedRoom = random.randint(101,199)
            elif self.amountpayed==100:
                self.assignedRoom = random.randint(201,299)
            elif self.amountpayed ==200:
                self.assignedRoom = random.randint(301,399)
            roomStatus=Client.checkIfOccupied(self.assignedRoom,roomsOccupied)
            if roomStatus is True:
                r.roomsOccupied.append(self.assignedRoom)
                
    def takeReservation(self):
        r=Room()
        temp=0
        while True:
            reservationtotal=0
            reservationsize=input("how many rooms would you like to reserve?")
            roomtype=r.determineRoomQuality()
            if 'Economy' in room:
                valuecoefficient=50
                secdeposit=25
            elif 'Economy Plus' in roomtype:
                valuecoefficient=100
                secdeposit=50
            elif 'Suite' in roomtype:
                valuecoefficient=200
                secdeposit=100
            reservationtotal=valuecoefficient*reservationsize + secdeposit
            reservationtotal+temp
            question=input("would you like to reserve any other rooms? (y/n)")
            if 'n' in question or 'N' in question:
                print("you have succsessfully booked your reservation, your total is {reservationtotal}")
                break
            else:
                temp=reservationtotal
            #save room # & name as diction bruh i told you to work on this not just put it in a comment

def main():
    c=Client()
    r=Room()
    mf=mainframe()
    #mainframe.addChargeToAmtOwed(mainframe,room,mainframe.reservationList)
    mainframe.welcomeScreen()
    

main()
