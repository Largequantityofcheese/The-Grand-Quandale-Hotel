#hey buddy make this code work
banList=["Joe Biden","Quandale Dingle"]

class client():
  def __init__(self):
    self.name=None
    self.assignedRoom=0
    self.contactInformation=None
    self.securityDeposit=0
    self.checkOutPayment=0
    self.hotelGiftBalance=0
    self.dietaryRestrictions=None
    self.timeOfCheckIn=None
    self.clientstatus="Respectable"
    
  def Inputnameandinfo(self):
    while True:
      self.name=input("please type your name: ")
      answer=input(f"{self.name}, is this your correct first and last name?")
      if "yes" in answer or "y" in answer:
        self.contactInformation=input("please input your phone number: ")
        response=input(f"{self.contactInformation}, is this your correct phone number?")
        if "yes" in answer or "y" in answer:
          break

  def checkClientStatus(self):
    if self.name in banList:
      self.clientstatus="Banned"
      print("You are not allowed in this establishment, security will be with you shortly.")

  def sellroom():
    return None

  def redeemGiftCard(self):
      self.hotelGiftBalance+=50
      
  def Refusecustomer():
   return None

def main():
    Inputnameandinfo()
    checkClientStatus()
    sellroom()
    #please stop saving pdfs in our database\

main()
