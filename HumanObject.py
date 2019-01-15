class Human(object):
    def __init__(self,name,hair_color,eye_color,height,weight,iq,gender,race):
        self.name=name
        self.hair_color=hair_color
        self.eye_color=eye_color
        self.height=height
        self.weight=weight
        self.iq=iq
        self.gender=gender
        self.race=race
    def introduce_self(self):
        print("Hello, my name is",self.name)
    def describe_self(self):
        print("I have "+self.hair_color+" hair")
        print("I have "+self.eye_color+" hair")
        print("I am ",self.height," tall")
        print("I weight ",self.weight," pounds")
        print("I am a "+self.race+" "+self.gender+" HumanE. With an IQ of "+self.iq)


def
kyla=Human("kyla","blonde","hazel",5,130,"idk","female","white")
kyla.name="Kyla"

kyla.introduce_self()
kyla.describe_self()
print()
personOne=Human("Person  One","color","color","height#","weight#","idk","some gender","some race")
personOne.introduce_self()
personOne.describe_self()
print()
personTwo=Human("Person Two","color","color","height#","weight#","idk","some gender","some race")
personTwo.introduce_self()
personTwo.describe_self()
print()
personThree=Human("Person Three","color","color","height#","weight#","idk","some gender","some race")
personThree.introduce_self()
personThree.describe_self()
print()
