import random

reservationList={}
roomsOccupied=[]

#emergency system (fire extinguishing, backup generators to hook into the power system)
#power system


class mainframe:
    def createDbMainframe():
        frame=[]
        rooms=[]

    def makePayment(self,room,nights):
        #c variable is a client object

        #add a charge for credit card transactions
        r=Room
        c=Client
        roomHierarchyClass={"Economy":50,"Economy Plus":100,"Suite":200}

        roomSecurityDeposit = {'Economy':25,'Economy Plus':50,'Suite':100}
        if room not in reservationList.values() and room not in roomsOccupied:
            r.roomCost=roomHierarchyClass[room]
        creditFee=1.05
        subTotal=r.roomCost*nights+roomSecurityDeposit[room]
        totalCost=subTotal*creditFee
        c.amountpayed=totalCost
        print(f"Your total cost for this experience comes up to ${totalCost}")

    def checkInClients(self):
        c=Client
        r=Room
        print("Please input your name using the pull-out keyboard on the kiosk: (First, Middle, Last)")
        clientName=input()
        c.name=clientName.split(", ")
        print(f"Hello {c.name[0]} {c.name[2]}. Please input the most convenient forms of contact: (separate with commas)")
        clientContact=str(input())
        c.contactInformation=clientContact.split(", ")
        print("If you have any dietary restrictions (i.e. allergies), please input them below:")
        clientDiet=input()
        c.dietaryRestrictions=clientDiet.split(", ")
        print("Thank you for registering, what type of room would you like:")
        print("Economy: $50, Economy Plus: $100, Suite: $200")
        roomtype=input()
        print("How many nights are you going to be staying?")
        nights=int(input())
        mainframe.makePayment(mainframe,roomtype,nights)

    def welcomeScreen(self):
        print("Hello customer, welcome to The Grand Quandale Hotel!")
        inputChoice=input("Are you making a reservation online or checking in at one of our locations? (check/reservation)")
        if "check" in inputChoice.lower():
            mainframe.checkInClients(mainframe)
        elif "reserv" in inputChoice.lower() or "reservation" in inputChoice.lower():
            Client.takeReservation(Client)

    def blippysArcade():
        print("")
        print("Welcome to Blippy Arcade. Would you like to play a game?")
        yaOrNah = input()
        #if barRating==10:
            #customMatch="Vs. Clevland Brown"
        if yaOrNah == "Yes":
            print("Would you like to play J-Money Simulator?")
            nahOrYa = input()
            if nahOrYa == "Yes":
                print("Ok, create some bars.")
                bars=input()
                barRating=random.randint(0,10)
                print(f"Wow, those were some bars, your score is: {barRating}/10")
                print("Hop on J-Money Sim again, yo")
            elif nahOrYa == "No":
                print("L Bozo + doesn't even want to play the J-Money simulator. Would you like to play the J-Money Adventure Game instead?")
                ouiOuNon = input()
                if ouiOuNon == "Yes":
                    print("Welcome to the J-Money Adventure Game, Player! You will face many challenges along the way. Are you ready?")
                    areYouPrepared = input()
                    if areYouPrepared == "Yes":
                        print("Your story begins in downtown chicago, where you just finished rapping to a large audience")
                        print("You are suddenly approached by some goons who are jealous of your ability to rap")
                        print("You have a mission, make it to the top of the rap game, and nobody will stop you")
                        print("Will you exert your authority by slapping the goons or will you take the pacifist approach?")
                        slapOrNah = input()
                        if slapOrNah == "Slap the goons":
                            print("You slap the goons very effectively, they all cower and shimmy away")
                            print("You have finished your buisness with the goons, and now you need to get back on the grind")
                            print("You have some song ideas in mind, each equally likely to take you straight to the top")
                            print("As you were thinking however, you are approached by a blind, deaf dog, who goes by the name Murray")
                            print("You see Murray, but he does not see you, for he is both blind and deaf")
                            print("You also notice Murray is dripping foam out of his mouth, meaning he's rabid")
                            print("Murray has drip as well. He is a threat and you need to take him out. Will you do so?")
                            takeMurrayOut = input()
                            if takeMurrayOut == "Yes":
                                print("You gave Murray a rap performance. Being so dissapointed in not being able to hear or see the performance, he spontaneously combusts")
                                print("After incinerating the blind, deaf dog, murray. you make your way to the studio, to produce some radical tunes. You choose the song know as:")
                                songChoice=input()
                                print(f"The song known as: {songChoice}. It's a smash hit, with the youth, showing up in all the tiktoks and fortinite compilations. You're on tour, and are in Utah, where you are rap battling a Mormon dude. He is eating green jell-o and funeral potatoes, with no coffee/tea, or alchohol/tobacco")
                                ("You decide to diss him with these bars:")
                                bars = input()
                                print("The morman is so incredibly roasted that he bursts off stage in tears. He feels as if the only person who could cheer him up now is John Smith himself")
                                print("This roast was great for your reputation, putting you now at #2 best rapper of all time, right behind your rival J-Blippy")
                                print("You now head to Ohio, Hell itself. This is where you will make your last stand against the menace that is J-Blippy. If you win this rap battle, you'll be #1, but if you die in the rap battle, you die in real life.")
                                print("You need to your best to beat J-Blippy, you'll need to bring the heat. You will diss him with these bars:")
                            else:
                                print("Murray bit you and you die instantly")
                        elif slapOrNah=="Shine your grills":
                            print("The goons have never seen such immaculate zinc grills, they quiver in sheer horror at your magnificent grills, purchased from ebay.com")
                        elif slapOrNah == "Take the pacifist approach":
                            print("The goons are not from downtown chicago as it turns out")
                            print("They are from England, and they decide to stab you to death")
                            #something stopped you

                    else:
                        print("L + coward + not even going to play J-Money Adventure Game")
                elif ouiOuNon == "No":
                    print("Sorry but we don't have any other games")
        elif yaOrNah == "No":
            print("Goodbye then, feel free to come back some other time")
            #j money need to start pulling his weight in the project
            #didn't ask + ratio
#7/10 this game is amazing, it reminds me of my childhood where i was forced to be immersed in raw sewage to find my father's car keys he dropped down the septic tank
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


    def foodService(self):
        tax=1.08
        print("Are you hungry? We have some delicacies from the local Dougmart")
        hungryOrNah = input()
        if hungryOrNah == "Yes":
            print("Welcome to Flavor Town, population you")
            print("We got chimken broth, frog legs, pickled soup, aged salmon, and mints stolen from another restaurant")
            print("What would you like to order?")
            daGrub = input()
            if daGrub == "Chimkin broth":
                print("That'll be $10")
                owedMoney = 10*tax
            elif daGrub == "Frog legs":
                print("That will be $20")
                owedMoney = 20*tax
            elif daGrub == "pickled soup":
                print("That'll be $15")
                owedMoney = 15*tax
            elif daGrub == "Aged salmon":
                print("Thatll be $40")
                owedMoney = 40*tax
            elif daGrub == "Mints":
                print("Thatll be $5")
                owedMoney = 5*tax
        return owedMoney

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

    def setRoomNumber(self, roomsOccupied,amountpayed):
        while True:
            r=Room
            if self.amountpayed <=50:
                self.assignedRoom = random.randint(101,199)
            elif self.amountpayed==100:
                self.assignedRoom = random.randint(201,299)
            elif self.amountpayed ==200:
                self.assignedRoom = random.randint(301,399)
            roomStatus=Client.checkIfOccupied(self.assignedRoom,roomsOccupied)
            if roomStatus is False:
                r.roomsOccupied.append(self.assignedRoom)
                break
                
    def takeReservation(self):
            reservationtotal=0
            print("What type of room would you like to reserve?")
            roomtype=input("Economy: $50, Economy Plus: $100, Suite: $200 ")
            print("How many nights are you going to be staying?")
            nights=int(input())
            mainframe.makePayment(mainframe,roomtype,nights)
            print("You have successfully booked your reservation.")
            if roomtype=="Suite":
                Client.setRoomNumber(Client,roomsOccupied,200)
            elif roomtype=="Economy Plus":
                Client.setRoomNumber(Client,roomsOccupied,100)
            elif roomtype=="Economy":
                Client.setRoomNumber(Client,roomsOccupied,50)
                    

def main():
    c=Client()
    r=Room()
    mf=mainframe()
    mainframe.welcomeScreen(mainframe)
    print("Are there any services you would like to use during your stay?")
    print("Cleaning Services, Air Conditioner, Arcade, Food Service")

main()

    #def fireSuppression(self, fireInBuilding, fireExtinguishersPresent):
    #    if fireInBuilding == True:
    #        if fireExtinguishersPresent == True:
    #            fireInBuilding = False
    #        elif fireExtinguishersPresent == False:
    #            fireInBuilding = True
    #            print("Evacuate the building or you might die")
    #    else:
    #        fireInBuilding = False
    #        if fireExtinguishersPresent == False:
    #            print("Fire extinguishers are needed in the building")
    
#    def airConditioner(self,temp):
#        if temp >= 72:
#            print("Would you like to turn the room temperature down to a normal 68 degrees?")
#            tempControl = input()
#            if tempControl == "Yes":
#                temp = 68
#            elif tempControl == "No":
#               temp = temp
#        elif temp <= 64:
#            print("Would you like to turn the room temperature up to a normal 68 degrees?")
#            tempControl = input()
#            if tempControl == "Yes":
#                temp = 68
#            elif tempControl == "No":
#                temp = temp
#        else:
#            temp = temp

#    def cleaningService(self,room,lemonPledge):
#        if room == "Dirty":
#            print("Hola. Soy aqui limpiar su habitacion, heuele a mierda de elphante")
#            if lemonPledge == "Present":
#                room = "Clean"
#            else:
#                room = "Dirty"
#                print("Necesitamos más Lemon Pledge")
#        else:
#            room = "Clean"


#    def backupGenerator(self,power,backupGenerator):
#        if power == True:
#            print("There is power in the building")
#            if backupGenerator == True:
#                print("We have a backup generator")
#            elif backupGenerator == False:
#                print("We need a backup generator")
#        elif power == False:
#            if backupGenerator == True:
#                power = True
#                print("We will use the backup generator")
#            elif backupGenerator == False:
#                power = False
#                print("L + no power")
