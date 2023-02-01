import random 

class mainframe:
    def __init__(self):
        #setting up individual room costs
        self.roomHierarchyClass={"Economy":50,"Economy Plus":100,"Suite":200}
        #security deposit room prices 
        self.roomSecurityDeposit = {'Economy':525,'Economy Plus':50,'Suite':100}
        
        #create a reservation list dictionary to store a one-to-one relationship between client and the room they are given at the time the reservation is made
        self.reservationList={}

    def getReservationList(self):
        return self.reservationList

    def createDbMainframe():
        frame=[]
        rooms=[]

    #c variable is a client object
    def addChargeToAmtOwed(self,total,c):
        #add a charge for credit card transactions
        return None

class Room(mainframe):
    def __init__(self):
        #integer values
        self.roomNumber=0
        self.roomCount
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


class Client(mainframe):
    def __init__(self):
        #string values
        self.name=[]
        #integer value
        self.assignedRoom=0
        #string value
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
    def checkIfOccupied(self,client,room,reservationList):
        
        if client in room:
            roomOccupied = True
        elif room in reservationList:
            roomOccupied = True
        else:
            roomOccupied = False


    def setRoomNumber(self, number, roomsOccupied):
        r=Room
        if self.amountpayed <=50:
            self.assignedRoom = random.randint(100,199)
        elif self.amountpayed==100:
            self.assignedRoom = random.randint(200,299)
        elif self.amountpayed ==200:
            self.assignedRoom = random.randint(300,399)
        roomsOccupied.append(self.assignedRoom)



    #r is a room object to assign a room to a specific client
    def assignARoom(self,room):
        return None

def main():
    #take reservations (room number, length of stay, cost, arrival, personal info, security deposit($50-200))
    #get client name
    c=Client(mainframe)
    r=Room(mainframe)
    print(c.accessReservationList())
    mainframe.createDbMainframe()
    #Room.determineRoomQuality(self)
    #addChargeToAmtOwed(self,total,c)
    #Inputnameandinfo()
    #checkClientStatus()
    #sellroom()

main()
