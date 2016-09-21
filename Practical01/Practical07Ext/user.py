"""
User class
"""

class User:

    def __init__(self,name,tacos=5,score=0):
        self.name = name
        self.tacos = tacos
        self.score = score

    def __str__(self):
        return "{} has {} tacos and a score of {}".format(self.name,self.tacos,self.score)

    def give_taco(self,receiver):
        self.tacos -= 1
        receiver.receive_taco()
        print("{} has Given a taco.".format(self.name))

    def receive_taco(self):
        self.score += 1
        print("{} has Received a taco.  Tacos: {},  Score {}".format(self.name,self.tacos,self.score))