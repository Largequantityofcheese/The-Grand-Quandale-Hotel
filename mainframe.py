class mainframe:
    def __init__(self):
        #setting up individual room costs
        self.roomHierarchyClass={"Economy":50,"Economy Plus":100,"Suite":200}
        


    def createDbMainframe():
        frame=[]
        rooms=[]
    
    #c variable is a client oject
    def addChargeToAmtOwed(self,total,c):
      #add a charge for credit card transactions
      return None

class Room(mainframe):
    def __init__(self):
        #integer values
        self.roomCount
        self.floorCount
        self.roomCapacity
        self.roomQuality
        #depending on quality of room
        #combination of quality (which floor and features)
        #subtract values from original quality score
        self.roomCost
        
        #True=room is open
        #False=room is occupied
        self.roomAvailability

    def determineRoomQuality(self):
      #score can be determined also by how person checking out left it
      roomQualityShare=[0,0,0]
      mf=mainframe
      if self.roomCost==mf.roomHierarchyClass[0]:
        roomQualityScore[0]=1
      elif self.roomCost==mf.roomHierarchyClass[1]:
        roomQualityScore[1]=1
      elif self.roomCost==mf.roomHierarchyClass[2]:
        roomQualityScore[2]=2
      return roomQualityScore
         
        

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
        
    def createReservation(self):
      return None

def main():
    #take reservations (room number, length of stay, cost, arrival, personal info, security deposit($50-200))
    #get client name 
    createDbMainframe()
    determineRoomQuality(self)
    addChargeToAmtOwed(self,total,c)

main()
