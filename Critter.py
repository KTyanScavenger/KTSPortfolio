# # #Object Att.
# # class Critter(object):
# #     def __init__(self,name):
# #         print("A new critter has been born.")
# #         self.name=name
# #
# #     def __str__(self):
# #         rep=self.name
# #
# #         return rep
# #
# #     def talk(self):
# #         print("Hi, I'm the instance of a class.")
# #
# # crit1 = Critter("Named")
# # if crit1=="Named":
# #     crit1.talk()
# # print(crit1)
# # crit2=Critter("Re-Named")
# # if crit2=="Named":
# #
# #     crit2.talk()
# # print(crit2)
# #
# # #Class Att.
# # class Critter2(object):
# #     """A virtual pet"""
# #     total=0
# #     def __init__(self,name):
# #         print("A critter has been born!")
# #         self.name=name
# #         Critter2.total += 1
# #
# #     def __str__(self):
# #         rep="Criter object\n"
# #         rep+= "name: "+ self.name + "\n"
# #         return rep
# #
# #     def talk(self):
# #         print("Hi. I'm",self.name,"\n")
# #     @staticmethod
# #     def status():
# #         print("\nThe total number of critters is: ", Critter2.total)
# # print("Accessing the class attribute Critter2.total:", end="")
# # print(Critter2.total)
# #
# # print("\nCreating critters")
# # crit1=Critter2("Name")
# # crit1.status()
# # crit2=Critter2("Tommy")
# # crit2.status()
# # crit3=Critter2("Jeremy")
# # crit3.status()
# # print("Accessing the class attribute Critter2.total:",end="")
# # print(Critter2.total)
# # Critter2.status()
# #
# # #CLASS ATTRIBUTE=Value that a class can hold
# # #OBJECT ATTRIBUTE=Name assigned to an object addition
# # #METHOD=Something that an object can do
# #
# #
# #
# #
#
# class Critter(object):
#     """A virtual pet"""
#     def __init__(self, name, mood):
#         print("A new critter has been born!")
#         self.name=name #public attribute
#         self.__mood=mood #private attribute
#
#     def talk(self):
#         print("\nI'm",self.name)
#         print("Right now I feel",self.__mood,"\n")
#
#     def __private_method(self):
#         print("This is a private method.")
#
#     def public_method(self):
#         print("This is a public method.")
#         self.__private_method()
#         crit1.name="Saboo"
#
# class Critter2(object):
#     """A virtual pet"""
#
#     def __init__(self, name, mood):
#         print("A new critter has been born!")
#         self.name = name  # public attribute
#         self.__mood = mood  # private attribute
#
#     def talk(self):
#         print("\nI'm", self.name)
#         print("Right now I feel", self.__mood, "\n")
#
#     def __private_method(self):
#         print("This is a private method.")
#
#     def public_method(self):
#         print("This is a public method.")
#         self.__private_method()
#         crit.__mood="bad mood"
#
# crit=Critter(name="Catch",mood="happy")
# crit1=Critter(name="Chase",mood="happy")
# crit.talk()
# crit1.talk()
#
# crit.public_method()
# crit1.public_method()
#
#
#
#

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name
    @property
    def name(self): #getter allows access to private attributes
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name cannot be empty.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        print("\nHi, I'm", self.name)


crit = Critter("Chase")
crit.talk()
print("My critter's name is", end="")
print(crit.name)

print("\nAttempting to change my Critter's name to Saboo...")
crit.name = "Saboo"
print("My critter's name is", end="")
print(crit.name)

print("\nAttempting to change my critter's name to empty string...")
crit.name = ""
print("My critter's name is:", end="")
print(crit.name)
