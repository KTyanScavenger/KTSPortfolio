#KYLA RYAN
#PROJECT
#2/19


#class player(object):
#    color =["red","blue","green"]

#    def __init__(self):
#        self.hair_color = self.chosecolor()
#    def chosecolor(self):
#     color = player.color[1]
#     return color
#
#x=player()
#print(x.hair_color)
from tkinter import *


import random
class Application(Frame):
    """Gui application which counts clicks"""
    def __init__(self, master):
        """initializing frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        # self.color_hair_gen = ["Blonde", "Brown", "Black", "Gray", "Red", "White", "Orange"]
        # self.color_hair_wak = ["Purple", "Pink", "Green", "Blue", "Teal", "Magenta", "Maroon"]
        #
        # self.color_skin_gen = ["Dark", "Pale", "Medium", "Tan", "Native"]
        # self.color_skin_wak = ["Blue", "Purple", "Red", "Yellow", "Green"]
        #
        # self.color_eye_gen = ["Green", "Hazel", "Brown", "Blue", "Black"]
        # self.color_eye_wak = ["Red", "Yellow", "Orange", "Pink", "Purple", "White"]

        self.genders = ["Male", "Female", "Undefined", "Undetermined", "Union"]
        self.races = ["Human", "Alien", "Animal", "Undefined", "Unidentified"]
        self.popularity = ["Highly", "Moderately", "Low", "Undetermined", "Unknown"]

        self.hair_len = ["Long", "Short", "None", "Mid", "Spiky"]
        self.hair_type = ["Trimmed", "Shaved", "Messy", "Punk", "Curly"]

        self.eye_num = ["Four+", "Three", "Two", "One", "No"]
        self.powers = ["Electricity", "Water", "Fire", "No", "Telepathy"]

        self.ranks = ["High", "Mid-Class", "Low", "Peasant", "Undetermined"]
        self.ending = ["Alive", "Dead", "Missing", "Mostly Dead", "On-The-Run"]

    def create_widgets(self):
        """create button, text, and entry widgets"""
        # construct instruction label
        self.inst_lbl = Label(self, text="Random Character Generator")
        self.inst_lbl.grid(row=0, column=1, columnspan=2, sticky=W)
        self.check_bx_lbl1=Label(self, text="Normal")
        self.check_bx_lbl2 = Label(self, text="Wacky")
        self.check_bx_lbl1.grid(row=1, column=1, sticky=NSEW)
        self.check_bx_lbl2.grid(row=1, column=2, sticky=NSEW)
        self.hair_color_lbl=Label(self, text="Hair Color: ")
        self.skin_color_lbl=Label(self, text="Skin Color: ")
        self.eye_color_lbl=Label(self, text="Eye Color: ")
        self.story_box=Text(self, width=35, height=10, wrap=WORD)
        self.hair_color_lbl.grid(row=2, column=0, sticky=W)
        self.skin_color_lbl.grid(row=3, column=0, sticky=W)
        self.eye_color_lbl.grid(row=4, column=0, sticky=W)
        self.story_box.grid(row=1, rowspan=20, column=4, sticky=E)
        self.name_box=Entry(self)
        self.name_box.grid(row=5, column=1, sticky=E)
        self.player_name=Label(self, text="Character Name: ")
        self.player_name.grid(row=5, column=0, sticky=W)

        self.color_hair_gen = ["Blonde", "Brown", "Black", "Gray", "Red", "White", "Orange"]
        self.color_hair_wak = ["Purple", "Pink", "Green", "Blue", "Teal", "Magenta", "Maroon"]
        self.color_skin_gen = ["Dark", "Pale", "Medium", "Tan", "Native"]
        self.color_skin_wak = ["Blue", "Purple", "Red", "Yellow", "Green"]
        self.color_eye_gen = ["Green", "Hazel", "Brown", "Blue", "Black"]
        self.color_eye_wak = ["Red", "Yellow", "Orange", "Pink", "Purple", "White"]

        self.hc=StringVar()
        self.hc.set(None)
        self.sk=StringVar()
        self.sk.set(None)
        self.ec=StringVar()
        self.ec.set(None)

        self.hair1_cb=Radiobutton(self, variable =self.hc, value =random.choice(self.color_hair_gen))
        self.hair2_cb=Radiobutton(self, variable =self.hc, value =random.choice(self.color_hair_wak))
        self.skin1_cb=Radiobutton(self, variable=self.sk, value=random.choice(self.color_skin_gen))
        self.skin2_cb=Radiobutton(self, variable=self.sk, value=random.choice(self.color_skin_wak))
        self.eye1_cb=Radiobutton(self, variable=self.ec, value=random.choice(self.color_eye_gen))
        self.eye2_cb=Radiobutton(self, variable=self.ec, value=random.choice(self.color_eye_wak))
        self.hair1_cb.grid(row=2, column=1, sticky=NSEW)
        self.hair2_cb.grid(row=2, column=2, sticky=NSEW)
        self.skin1_cb.grid(row=3, column=1, sticky=NSEW)
        self.skin2_cb.grid(row=3, column=2, sticky=NSEW)
        self.eye1_cb.grid(row=4, column=1, sticky=NSEW)
        self.eye2_cb.grid(row=4, column=2, sticky=NSEW)

        self.sumbit=Button(self, height=2, width=3, text="Submit button", command=self.submit)
        self.sumbit.grid(row=20, rowspan=2, column=0, columnspan=3, sticky=NSEW)
    def submit(self):


        hair_color=self.hc.get()
        skin_color=self.sk.get()
        eye_color=self.ec.get()
        length = random.choice(self.hair_len)
        type = random.choice(self.hair_type)
        eyes = random.choice(self.eye_num)
        gender = random.choice(self.genders)
        rank = random.choice(self.ranks)
        pop = random.choice(self.popularity)
        race = random.choice(self.races)
        power = random.choice(self.powers)
        fate = random.choice(self.ending)
        name = self.name_box.get()
        x = Player(hair_color, skin_color,eye_color,length,type,eyes,gender,rank,pop,race,power,fate,name)
        STORYLN = "One day on a desolate planet, a child was born. A(n) "+str(x.genders)+" "+str(x.races)\
            +" child with " +str(x.eye_num) +" "+str(x.color_eye_gen)+" eyes and "+str(x.color_hair_gen)+" "+str(x.hair_len)+" "+\
                  str(x.hair_type) +" hair. As the child grew, they rose to the "+str(x.rank)+ " "+ \
                  "rank in society. Their popularity with the native people was at the astonishing "\
            +str(x.popularity) +" popularity, forcing them to learn "+str(x.powers)+" power. " \
            " The people grew to fear " +str(x.names) +". Innevitably, " +str(x.names) +\
                  "'s fate was the tragic ending of " + str(x.ending)


        self.story_box.delete(0.0, END)
        self.story_box.insert(0.0, STORYLN)

# #Define lists the object call pull attributes from
# color_hair_gen=["Blonde","Brown","Black","Gray","Red","White","Orange"]
# color_hair_wak=["Purple","Pink","Green","Blue","Teal","Magenta","Maroon"]
#
# color_skin_gen=["Dark","Pale","Medium","Tan","Native"]
# color_skin_wak=["Blue","Purple","Red","Yellow","Green"]
#
# color_eye_gen=["Green", "Hazel", "Brown", "Blue", "Black"]
# color_eye_wak=["Red","Yellow","Orange","Pink","Purple","White"]
#
# genders=["Male","Female","Undefined","Undetermined","Union"]
# races=["Human","Alien","Animal","Undefined","Unidentified"]
# popularity=["Highly", "Moderately", "Low", "Undetermined", "Unknown"]
#
# hair_len=["Long", "Short", "None", "Mid", "Spiky"]
# hair_type=["Trimmed", "Shaved", "Messy", "Punk","Curly"]
#
# eye_num=["Four+", "Three", "Two", "One", "No"]
# powers=["Electricity", "Water","Fire","No","Telepathy"]
#
# ranks=["High", "Mid-Class","Low","Peasant","Undetermined"]
# ending=["Alive","Dead","Missing","Mostly Dead","On-The-Run"]


class Player(object):
    def __init__(self, hair_color, skin_color, eye_color, length, type, eyes, gender, rank, pop, race, power, fate, name):

    #Define usable functions and give them callable names
        self.color_hair_gen = hair_color
        #self.color_hair_wak = self.choose_color_hair_wak()
        self.hair_len = length
        self.hair_type = type

        self.color_skin_gen = skin_color
        #self.color_skin_wak = self.choose_color_skin_wak()

        self.color_eye_gen = eye_color
        #self.color_eye_wak = self.choose_color_eye_wak()
        self.eye_num = eyes

        self.genders = gender
        self.races = race

        self.popularity = pop
        self.rank = rank

        self.powers = power
        self.ending = fate
        self.names = name
    # def choose_color_hair_gen(self):
    #     while True:
    #         hair_choice=(input("Do you want 1. Generic Hair Color, or 2. Wacky Hair Color? Enter a number (1/2) "))
    #         if hair_choice=="1":
    #             color1=random.choice(color_hair_gen)
    #             print(color1)
    #             return color1
    #
    #         elif hair_choice=="2":
    #             self.choose_color_hair_wak()
    #             break
    #         else:
    #             print("That is not a valid input.")
    # def choose_color_hair_wak(self):
    #     color1=random.choice(color_hair_wak)
    #     print(color1)
    #     return color1
    #
    # def choose_hair_len(self):
    #         input("Press any number to get a hair length: ")
    #         length=random.choice(hair_len)
    #         print(length)
    #         return length
    # def choose_hair_type(self):
    #     input("Press any number to get a hair type/style: ")
    #     type=random.choice(hair_type)
    #     print(type)
    #     return type
    # def choose_color_skin_gen(self):
    #     while True:
    #         skin_choice=(input("Do you want 1. Generic Skin Color, or 2. Wacky Skin Color? Enter a number (1/2) "))
    #         if skin_choice=="1":
    #             color2=random.choice(color_skin_gen)
    #             print(color2)
    #             return color2
    #
    #         elif skin_choice=="2":
    #             self.choose_color_skin_wak()
    #             break
    #         else:
    #             print("That is not a valid input.")
    # def choose_color_skin_wak(self):
    #     color2=random.choice(color_skin_wak)
    #     print(color2)
    #     return color2
    # def choose_color_eye_gen(self):
    #     while True:
    #         eye_choice=(input("Do you want 1. Generic Eye Color, or 2. Wacky Eye Color? Enter a number (1/2) "))
    #         if eye_choice=="1":
    #             color3=random.choice(color_eye_gen)
    #             print(color3)
    #             return color3
    #
    #         elif eye_choice=="2":
    #             self.choose_color_eye_wak()
    #             break
    #         else:
    #             print("That is not a valid input.")
    # def choose_color_eye_wak(self):
    #
    #     color3=random.choice(color_eye_wak)
    #     print(color3)
    #     return color3
    #
    # def choose_eye_num(self):
    #     input("Press any number to get a number of eyes: ")
    #     eyes=random.choice(eye_num)
    #     print(eyes)
    #     return eyes
    # def choose_gender(self):
    #     input("Press any number to get a gender: ")
    #     gender=random.choice(genders)
    #     print(gender)
    #     return gender
    # def choose_rank(self):
    #     input("Press any number to get a rank in society: ")
    #     rank=random.choice(ranks)
    #     print(rank)
    #     return rank
    # def choose_popularity(self):
    #     input("Press any number to know your popularity with the people: ")
    #     pop=random.choice(popularity)
    #     print(pop)
    #     return pop
    # def choose_race(self):
    #     input("Press any number to know your race: ")
    #     race=random.choice(races)
    #     print(race)
    #     return race
    # def choose_power(self):
    #     input("Press any number to know your power: ")
    #     power=random.choice(powers)
    #     print(power)
    #     return power
    # def choose_ending(self):
    #     input("Press any number to know your fate! ")
    #     fate=random.choice(ending)
    #     return fate
    #
    # def names(self):
    #     name=input("Enter a name for your character: ")
    #     return name
root=Tk()
#
root.title("Character Creator")
root.geometry("750x750")
#canvas=Canvas(root, width=250, height=250)
#canvas.pack()
#img=ImageTk.PhotoImage(file="")
#canvas.create_image(20,20, anchor=NW, image=img)


app=Application(root)



root.mainloop()


