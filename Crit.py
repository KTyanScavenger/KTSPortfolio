import time
import random
old_time=time.time()
class Critter(object):

    def __init__(self, name):
        print("A new critter has been born.")
        self.name = name
        self.hunger = random.randint(0, 11)
        self.boredom=random.randint(0, 11)



    def __pass_time(self):
        global old_time
        current_time = time.time()
        x=time.time()-old_time
        if time.time()-old_time>5:
            self.hunger+= 0.5*x
            self.boredom+=0.5*x
        old_time = current_time

    def play(self):
        self.__pass_time()
        if self.boredom>=5:
            print(self.name,"wants to play a game!")
            a=input("Do you want to play with your critter? (y/n)")
            if a.capitalize()=="Y":
                b=input("How long do you want to play with your critter?")
                if b >= str(5):
                    self.boredom -= int(5)
                    print("You played with", self.name,"!")
                    self.boredom-=5
                    if self.boredom>=0==True:
                        self.boredom=0





    def talk(self):
        self.__pass_time()
        print(self.name)
        print(self.mood)
        print(self.hunger)
        print(self.boredom)


    def eat(self):
        self.__pass_time()
        if self.hunger>=5:
            print(self.name,"wants to eat.")
            c=input("How much food do you want to feed your critter? ")
            if c>=str(5):
                self.hunger-=int(5)
            else:
                self.hunger-=int(3)




    @property
    def mood(self):
        self.happiness = self.hunger+self.boredom
        if self.happiness<=5:
            mood="Happy"
        elif self.happiness<=10:
            mood="Okay"
        elif 11<=self.happiness<=15:
            mood="Frustrated"
        else:
            mood="Mad"
        return mood

def main():
    name=input("What do you want to name your critter? ")
    while True:
        if name!="":
            break
    crit=Critter(name)
    choice=None
    while choice!=0:
        crit.talk()

        choice=int(input("Enter a number to interact with your critter(1, 2, 3, or 0 to exit): "))
        if choice==1:
            crit.talk()
        elif choice==2:
            crit.eat()
            if crit.hunger<=5:
                print(name, "is not hungry right now.")
        elif choice==3:
            crit.play()
            if crit.boredom<=5:
                print(name, "is not bored right now.")
        elif choice==0:
            break
        else:
            print("That is not a good choice.")
    print("Goodbye!")




main()





