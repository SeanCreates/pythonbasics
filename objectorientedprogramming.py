class Travel:
    def __init__(self, name, when, why) :
        self.name = name
        self.when = when
        self.why = why

    def travel(self):
        print(f"A country I really want to travel to is {self.name}"
              f" and I'd really like to go on {self.when} for the reasons :{self.why} ")


myobj = Travel("Santorini,Greece", "April,2035", "The Blue skies and sandy "
                                                 "beaches:)")
myobj2 = Travel("Italy", "September,2030", "Sasha and Ivy really wants to go"
                                           " and its my birthday.")
myobj.travel()
myobj2.travel()