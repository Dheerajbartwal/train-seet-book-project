# create a class Train which has method to book a ticket, get_status(no of seets) and get fare_information of trains running under indian railway

class Train:
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def bookTicket(self):
        if(self.seats>0):
            self.seats = self.seats-1

            print(f"your seet is booked and your seet number is {self.seats}")
        else:
            print("kindly book tatkal..")
        
    def checkStatus(self):
        # self.seats = self.seats-self.
        print(f"total seats are remaining are  {self.seats}")        

    def fareInformation(self):
        print(f"yout ticker price is {self.fare}")

a= Train("rajdhani",30,90)
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.bookTicket()


a.checkStatus()
a.fareInformation()
print("Happy journey!")