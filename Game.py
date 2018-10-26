#Kyla Ryan
#10/18

#start
global machete

global flashlight

global product

global rune
import random
def start():
    print("Your plane has landed after a tiring trip taking literally hours.\n"
          "The landing was a bit rough, but you were landing on the beach. A\n"
          "calm breeze moved through the sands to wake up the waves. It was \n"
          "enjoyable. You needed some time for yourself, so you go towards  \n"
          "the water.")
    print("""
-----------------------------------------------------------------
  O
 OOO                  O
OOOOO                OOO                
                    OOOOO                                    OO
                                                            OOOO
                                                           OOOOOO
                                                          OOOOOOO
       


-----------------------------------------------------------------
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyyyyyyyyssssssoo+//:--:
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssooooo++++oo++/' --;^/ ,-__
hhhhhhhyyyyssssoo+++/++osooo++/+//:://///:::-----./ / --o\ o-\ \|
yysssooo++//:--:::////+++o+++//:---............../-/-/|o|-|\-\\||
:oooo+/++ooo++/://+///::://:::--.```````````...'`  ` |-|   `` '::
:::--::///+++oo+++++/::----...```````````.....-:::---|-|::+oo+/--
::::://++oo++//::--.-.....`..```````.....---::-------|-|:/+soo+/:
---://:/++oo++//:--.```````'''``````...--::------:+++|-|O++.-:/:/
+++oo++/////:/::-..`.```````````..----.....---://+///|-(\,__-..--
:::----------........``````....---..-...------:/-[...|-|\--]-....
-------.-.........``..```..--...--..-::-::-.-.:.--+so-..--.......
----........```````.-....-......--:/:-/::...-::::/::--...........
.........``````....--.-..`.--.-.--::/:--..-::/:...........--..--:
-..-.`````..-......`.-....-.-../::-::/o+:/:///---...--+--...:-:/o
""")
    input_water()
   


def input_water():
    
    water_app=["a","A","b","B"]
    input_water=input("You have one of two options:\n"
                      "A. Walk along the beach.\n"
                      "B. Look around.\n"
                      "")
    if input_water=="A" or input_water=="a":
        print("You walk along the beach and step on something hard.")
        input_rune()
    elif input_water=="B" or input_water=="b":
        print("You look around, noticing something in the water.")
        input_shell()
    else:
        input_water()
        
def beach():
    beach_app=["A","B","a","b"]
    input_beach=input("You have one of two options:\n"
          "A. Yes.\n"
          "B. No. \n"
          "")
    if input_beach=="A" or input_beach=="a":
        print("You walk along the beach and step on something hard.")
        input_rune()
    elif input_beach=="B" or input_beach=="b":
        print("Do you want to go to the plane hangar?")
        input_go_hangar()
    else:
        beach()
    
    
def input_rune():
    global rune
    in_rune_app=["A","a","B","b"]
    input_rune=input("You have one of two options:\n"
                     "A. Just a rock.\n"
                     "B. Pick it up.\n"
                     "")
    #Leaves Rune
    if input_rune=="A" or input_rune=="a":
        print("You ignore what you stepped on and find nothing else to do.\n"
              "The next place to go is the plane hangar, do you want to go there?\n"
              "")
        rune=False
        input_go_hangar()
    #picks up rune
    elif input_rune=="B" or input_rune=="b":
        rune=True
        print("You pick up what you stepped on, finding out that is is a rune\n"
              "with lovely engravings. There is nothing else to do here. Do you\n"
              "want to go to the plane hangar?\n"
              "")
        print("""
           ,aP8b    _,dYba,       ,adPb,_    d8Ya,
         ,aP"  Yb_,dP"   "Yba, ,adP"   "Yb,_dP  "Ya,
       ,aP"    _88"         )888(         "88_    "Ya,
     ,aP"   _,dP"Yb      ,adP"8"Yba,      dP"Yb,_   "Ya,
      Yb _,dP8    Yb  ,adP"   8   "Yba,  dP    8Yb,_ dP
       YdP" dP     YbdP"      8      "YbdP     Yb "YbP
        8aaa8aaaaaaaa8aaaaaaaa8aaaaaaaa8aaaaaaaa8aaa8I
       d8a, Ya      d8b,      8      ,d8b      aP ,a8b
      dP "Ya "8,   dI "Yb,    8    ,dP" Ib   ,8" aP" Yb
     Y8,   "YaI8, ,8'   "Yb,  8  ,dP"   `8, ,8IaP"   ,8P"
      "Yb,   `"Y8ad'      "Yb,8,dP"      `ba8P"'   ,dP"
        "Yb,    `"8,        "Y8P"        ,8"'    ,dP" """)
        input_go_hangar()
    else:
        input_rune()
              
    
def input_shell():
    in_shell_app=["a","A","B","b"]
    input_shell=input("You have one of two options:\n"
                      "A. Probably just a shell.\n"
                      "B. Pick it up.\n"
                      "")
    if input_shell=="A" or input_shell=="a":
        print("You ignore what you saw and keep walking along the shore. Do you want\n"
              "to walk along the beach?"
              "")
        beach()
    elif input_shell=="B" or input_shell=="b":
        print("You go to pick up what you saw, and alas, it was just a shell. \n"
              "There is nothing else to do here. Do you want to go to the beach?\n"
              "")
        print("""           _.-''|''-._
        .-'     |     `-.
      .'\       |       /`.
    .'   \      |      /   `.
    \     \     |     /     /
     `\    \    |    /    /'
       `\   \   |   /   /'
         `\  \  |  /  /'
        _.-`\ \ | / /'-._
       {_____`\\|//'_____}
               `-'""")
        beach()
        
    else:
        input_shell()
    
def input_go_hangar():
    in_shell_app=["A","a","B","b"]
    input_hangar=input("You have one of two options:\n"
                       "A. Yes.\n"
                       "B. Yes.\n"
                       "")
    if input_hangar=="A" or input_hangar=="a" or input_hangar=="b" or input_hangar=="B":    
        print("You go to the plane hangar.")
        plane_hangar()
    else:
        input_go_hangar()
              

def plane_hangar():
    print("You walked inside to the Plane Hangar. You've been here before, \n"
          "and knew where you were going. There were many new faces about.")
    in_hangar_app=["A","a","b","B"]
    input_hangar2=input("You have one of two options:\n"
                       "A. Go to your office.\n"
                       "B. See if your boss gave you anything in your office.\n"
                       "")
    if input_hangar2=="A" or input_hangar2=="a" or input_hangar2=="B" or input_hanger2=="b":
        print("You walk to your office, seeing a clutter of things and a letter on your desk.")
        office()
    else:
        plane_hangar()
              
def office():
    in_office_app=["a","A","b","B"]
    input_office=input("You have one of two options:\n"
                       "A. Rummage around.\n"
                       "B. Read a letter from your boss.\n"
                       "")
    if input_office=="A" or input_office=="a":
        print("You decide to tidy up a bit and rummage around, finding a machete.\n"
              "What do you do?\n"
              "")
        rummage()
    elif input_office=="B" or input_office=="b":
        letter()       
    
    else:
        office()
def letter():

        global product
        print("You pick up the letter from your boss, reading the information.")
        print("--------------\n"
              "| \        / |\n"
              "|   \    /   |\n"
              "|     \/     |\n"
              "--------------")
        print("The letter reads:\n"
              "'Hello pilot,\n"
              "Glad you could make it, sad I won't be able to see you. Listen,\n"
              "we want to make sure the island is safe before we stretch out  \n"
              "our base. There's none on this base I'd trust more than you. I \n"
              "know you can do it. We're all counting on you.\n"
              "                        -Sgt. Roger Dunstock'\n"
              "'P.S. Take the gun found near this letter. You'll need it.'")
        print("You pick up the gun.")
        product=True
        print("There's nothing else to do here, do you want to keep looking? ")
        keep_looking()
def rummage():
    in_rummage_app=["A","a","B","b"]
    input_rummage=input("You have one of two options:\n"
                        "A. Pick it up.\n"
                        "B. Leave it.\n"
                        "")
    if input_rummage=="a" or rummage=="A":
        global machete
        machete=True
        print("You pick up the machete and read the letter from your boss.\n"
              "")
        print("""       |______________
[======|______________>
       |
       '""")
        
        letter()
    elif input_rummage=="b" or rummage=="B":
        print("You leave the machete and read the letter from your boss.")
        letter()
              
def keep_looking():

    
    in_look_app=["A","a","B","b"]
    input_look=input("You have one of two options:\n"
                     "A. Yes.\n"
                     "B. No.\n"
                     "")
    if input_look=="A" or input_look=="a":
        print("You find a flashlight, and it appears to be working. Do you pick\n"
              "it up?\n"
              "")
        flashlight()
    elif input_look=="B" or input_look=="b":
        print("You decide to move on. There's nothing else here.\n"
              "Do you go to the rest of the hangar?")
        rest_hangar()
        
    
def flashlight():
    global flashlight
    in_flash_app=["A","B","b","a"]
    input_flash=input("You have one of two options:\n"
                      "A. Pick it up.\n"
                      "B. Leave it be.\n"
                      "")
    if input_flash=="A" or input_flash=="a":
        flashlight=True
        print("You pick up the flashlight. There is nothing else to do here,\n"
              "do you want to go to the rest of the hangar?")
        print("""			
                      _.----.
    .----------------" /  /  \
   (
    `----------------._\  \  /
                       "----'""")
        rest_hangar()
    elif input_flash=="B" or input_flash=="b":
        print("You leave the flashlight there. Do you want to go to the rest of the hangar?")
        rest_hangar()
def rest_hangar():
    rest_hangar_app=["A","a","B","b"]
    input_rest_hangar=input("You have one of two options:\n"
                            "A. Yes.\n"
                            "B. No. \n"
                            "")
    if input_rest_hangar=="a" or input_rest_hangar=="A":
        print("You walk over to a newbie pilot, hoping to make a friend or strike a conversation.\n"
              "He gives you a look and hands you his jacket. This fresh-meat thinks you're an \n"
              "errand boy.\n"
              "")
        pilot()
    elif input_rest_hangar=="b" or input_rest_hangar=="B":
        print("There isn't anything else to do here. Want to go to the jungle?")
        jungle()
    else:
        rest_hangar()
        
        
        
def pilot():
    in_pilot_app=["A","a","B","b"]
    input_pilot=input("You have one of two options:\n"
                      "A. Take the jacket, might as well look look.\n"
                      "B. Ain't no errand boi! Throw it back at him.\n"
                      "")
    if input_pilot=="a" or input_pilot=="A":
        print("You take the jacket and put it on as the pilot walks away.\n"
              "Too bad for him, this is a snazzy looking jacket.\n"
              "Are you ready to go to the jungle?")
        print("""          ,..,
       .-//||\\-.
      / ,      , \
     /  ;      ;  \
     './|      |\.'
        |      |
        |      |
        ||||||||
        `"===="`""")
        jungle()
    elif input_pilot=="B" or input_pilot=="b":
        print("You throw the jacket back at the pilot, making him irritated.\n"
              "He throws it right back.")
        outburst()
    else:
        pilot()
    
def outburst():
    in_outburst_app=["A","B","a","b"]
    input_outburst=input("You have one of two options:\n"
                      "A. Keep the jacket; he didn't need it anyways.\n"
                      "B. Just walk away.\n"
                      "")
    if input_outburst=="A" or input_outburst=="a":
        print("You take the jacket and put it on as the pilot walks away.\n"
              "Too bad for him, this is a snazzy looking jacket.\n"
              "Are you ready to go to the jungle?")
        print("""          ,..,
       .-//||\\-.
      / ,      , \
     /  ;      ;  \
     './|      |\.'
        |      |
        |      |
        ||||||||
        `"===="`""")
        jungle()
    elif input_outburst=="B" or input_outburst=="b":
        print("You drop the jacket and walk away. He should respect his elders.\n"
              "Are you ready to venture into the jungle?")
        jungle()
    else:
        outburst()
    
def jungle():
    jungle_app=["A","a","B","b"]
    input_jungle=input("You have one of two options:\n"
                           "A. YES.\n"
                           "B. YES.\n"
                           "")
    if input_jungle=="A" or input_jungle=="B" or input_jungle=="a" or input_jungle=="b":
        print("You have entered the jungle. Trees and vines are everywhere, and don't\n"
          "seem to be getting any less. You notice two paths ahead, one in the cliffs\n"
          "the other through the trees. Which do you pick?\n"
          "")
    BIG_DECISION()
    #THIS IS WHERE THE PLAYER CHOOSES THEIR ROUTE!!!!!
def BIG_DECISION():
    dec_app=["A","a","b","B"]
    input_dec=input("A. The Cliffs.\n"
                    "B. The Trees.\n"
                    "")
    if input_dec=="A" or input_dec=="a":
        print("You brush away some vines which seem strategically placed.\n"
              "What do you do?")
        cliff_one()
    elif input_dec=="B" or input_dec=="b":
        print("You enter into the trees, finding a clean path. Do you keep going?")
        tree_one()
    else:
        BIG_DECISION()
def cliff_one():
    global machete
    co_app=["A","B","a","b"]
    input_co=input("You have one of two choices:\n"
                   "A. Cut vines with the machete.\n"
                   "B. Brush away.\n"
                   "")
    if input_co=="A" and machete==True or input_co=="a" and machete==True:
        print("You cut away the vines, but the machete broke in the process.\n"
              "Tough vines, amirite?\n"
              "The vines have been removed, and a cave revealed. \n"
              "You go in the cave because there is no other way around.\n"
              "The cave is too dark, what do you do?")
        machete=False
        cliff_two()
        
    elif input_co=="A" and machete!=True or input_co=="a" and machete!=True:
        print("Sorry, you don't have that with you.")
        cliff_one()
    elif input_co=="B" or input_co=="b":
        print("You easily brush the vines away, revealing a cave. \n"
              "You go in the cave because there is no way around.\n"
              "The cave is too dark, what do you do?")
        cliff_two()
    else:
        cliff_one()
def tree_one():
    to_app=["A","B","a","b"]
    input_to=input("You have one of two options:\n"
                   "A. Yes.\n"
                   "B. No.\n"
                   "")
    if input_to=="A" or input_to=="a":
        print("You keep moving, and notice the trees getting thicker. Keep going?")
        tree_two()
    elif input_to=="B" or input_to=="b":
        print("You turn behind you, but the path has disappeared and is nothing but trees.\n"
              "You must keep going, and notice the trees getting thicker as you venture in.\n"
              "Keep going?")
        tree_two()
    else:
        tree_one()
def cliff_two():
    global flashlight
    ct_app=["A","B","b","a"]
    input_ct=input("You have one of two options:\n"
                   "A. Use flashlight.\n"
                   "B. Keep blindly walking.\n"
                   "")
    if input_ct=="A" and flashlight==True or input_ct=="a" and flashlight==True:
        print("You turn the flashlight on, and the cave is illuminated. Keep going?")
        cliff_three()
    elif input_ct=="A" and flashlight!=True or input_ct=="A" and flashlight!=True:
        print("Sorry, you don't have that with you.")
        cliff_two()
    elif input_ct=="B" or input_ct=="b":
        print("You keep going through the dark cave. Do you want to keep going?")
        cliff_three()
    else:
        cliff_two()

def tree_two():
    tt_app=["A","a","B","b"]
    input_tt=input("You have one of two options:\n"
                   "A. Yes.\n"
                   "B. No\n"
                   "")
    if input_tt=="A" or input_tt=="a":
        print("You keep going, and come to a stopping point. The trees are too thick.\n"
              "You need to cut the trees. What do you do?\n"
              "")
        tree_three()
    elif input_tt=="B" or input_tt=="b":
        print("The only way is forward. You keep going, and come to a stopping point.\n"
              "The trees are too thick. You need to cut the trees. What do you do?\n"
              "")
        tree_three()
    else:
        tree_two()

def cliff_three():
    ct_app=["A","B","a","b"]
    input_ct=input("You have one of two options:\n"
                   "A. Keep going.\n"
                   "B. Keep going, I ain't no wimp.\n"
                   "")
    if input_ct=="A" or input_ct=="B" or input_ct=="a" or input_ct=="b":
        print("You keep going, as an eerie feeling enters your stomach.\n"
              "Nothing lies ahead but a swirling tunnel.\n"
              "What do you do?\n"
              "")
        tree_four()
    else:
        cliff_three()
def tree_three():
    global machete
    trt_app=["A","a","B","b"]
    input_trt=input("You have one of two options:\n"
                    "A. Use machete to cut trees.\n"
                    "B. Try without it.\n"
                    "")
    if input_trt=="A" and machete==True or input_trt=="a" and machete==True:
        print("""
................................-*#@**#+=@W@++=###=+.::........................

.............................:**=:=#++#=***#:==*+:==:==*..-....................

.........................+.*=::++*=+==:==**==++#*#=++*##=:+....................

.......++.*........*:=-::..---:---#++*@W===*****@+@+*==#*+==:..................

......-:..*-...-++::*:.......-:*-+**=**#=##*-*@*#***===#*+*==*+................

.....-=-..**:*=::*--:......:+-***+*##@+**==:@*@@#*+:+#:@=+=#*W-.....:+.........

.....:@*:-.=:-..==-:.......-:==**#*#=@:+#:+@@=+*#:+*###=#=@*@@-.+@:+=..........

......-#===-..-=:----......*+:=+*=#==:-*-+##+.++=:*#+W+=+:#:#@*#=+@=...........

.......-#--...:==..--...-+-:-++*#W=*++*=.:#@:**I AM A BOAR*W+-*W#*...........

......:+.:..*::#=::.....+-:..+**#=*=+#W@::*=...-.**=+-......-=@:#+++...........

.....-=.+-..+-:#+......+.-*-*.-*@=#**-=++-.-..:.:*.-*...+*=+..:@:*.............

.....*-..+*--::....-+*..:.....-..#=@#+.:*+-+-..:@@#:-*::::@@**#=...............

.....-@.-@=#-++++-*=W:.......+....@W+=*:-*:*+:-+*:-:-=+-:-..:#++..*:...........

......*-.-+*@W:++=-*+......-.....-=#=+--+.+**:.--++--*+*::++:::=.**-...........

..--....*--.=..:@.-::*#==W=+...-W...W=-+::+-......-#=########@@........::+++...

..--....-#**+#..=:....*-........-W...W=..........--:*.:=#=@==:::......:........

....*....==@+*:.*#:.:*#-.-...::..-W...W@........*-..=-..++#............-:......

.:-.......-*=*:.=##:-+*@......+.............-=-.....:*:::*#*........:--=.:-....

........-:-......:@*--+*=-....+:...........+-........@+:+++*#:.....-+*-.+......

..................*+==:+.@.......--.........+:........#*+@#+=*-..........+.....

...................@*@*=:+=-----.................-:-.-+**==*-+*................

""")
        print("You use the machete, cutting the trees just enough to get through.\n"
              "However, the machete has broke in two, unusable. Typical Great Value brands.\n"
              "You keep going and begin to hear rustling in the trees as you near a large opening.\n"
              "There stands what appears to be a Giant Boar. What do you do?!\n"
              "")
        tree_four()
    elif input_trt=="A" and machete!=True or input_trt=="a" and machete!=True:
        print("Sorry, you don't have that with you.")
        tree_three()
    elif input_trt=="B" or input_trt=="b":
        print("The trees are too thick to get through without the machete.")
        if machete==True:
            print("You have the machete.")
            tree_three()
        elif machete!=True:
            print("You don't have that, and are stuck in the jungle...\n"
              """ _______  _______  _______  _______           _______  _______ 
(  ____ \(  ___  )(  ____ )(  ____ \|\     /|(  ____ \(  ____ )
| (    \/| (   ) || (    )|| (    \/| )   ( || (    \/| (    )|
| (__    | |   | || (____)|| (__    | |   | || (__    | (____)|
|  __)   | |   | ||     __)|  __)   ( (   ) )|  __)   |     __)
| (      | |   | || (\ (   | (       \ \_/ / | (      | (\ (   
| )      | (___) || ) \ \__| (____/\  \   /  | (____/\| ) \ \__
|/       (_______)|/   \__/(_______/   \_/   (_______/|/   \__/
                                                               """)
        end()
    else:
        tree_three()

def cliff_four():
    cf_app=["A","a","b","B"]
    input_cf=input("You have one of two options:\n"
                   "A. Keep going.\n"
                   "B. Keep going though I feel sick.\n"
                   "")
    if input_cf=="a" or input_cf=="A" or input_cf=="B" or input_cf=="b":
        print("You keep going, only stopping when a large roar shakes the tunnel.\n"
              "A light is finally visible at the end of the tunnel, you rush towards\n"
              "it, unaware of the monstrous bat waiting for you.\n"
              """............................+@:.-++..........++-.:@+...........................

.........................+:*@@#@=-+=#+....+#=+-=@#@@*:+........................

........................:@@@===#@@@@@@#**#@@@@@@#===@@@:.......................

.......................*-@@==###@====*=##=*==##@###==@@-*......................

......................=@@#*==[   ]=#===###==#[   ]====*#@@=....................

......................=-@#+*=*[ ]*=I AM A BAT###[ ]=*=*+#@-=...................

......................-*#@****=.:**=#=*==*=#=**:.=****@#*-.....................

..........#:............-@@**=******#     ##******=**@@-............:#.........

........:#@-.......-....+@#=@#====            ====@#=#@+....-.......-@#:.......

.......*#=#*......::+#@#:-#*@=*==*   ::**::   ===*=@*#-:#@#+::......*#=#*......

......+@===@*.......-@@@@@=:*=*###@ @==##=#@ @###*=*:=@@@@@-.......=@===@+.....

.....-@@#===@@=-...:#@###@@@#@=******************=@##@@##=@#:...-=@@===#@#-....

.....#@#@#==#@@@@@@#@#=####@@@@@@@@@@@@@@@@@@@@@@@@@@######@@@@@@@@#==#@=@#....

....+###=#==###@#@@@@@#==#+=#@#=*=*#@@*##*@@=*=*=#@#=+#==#@@@@@#@###==@=###+...

....##=@=##==#@#=@@=@####@###@##==#@@=*##*=@@#=###@###@####@=@@=#@#==@#=@=##...

...-@#=#=##====#@#=##=#*###@--#####==#=##=#==#####--@###*####=#@#====##=#=#@-..

...:@#=#==@@##=#==#####=##@:...+@@#@#@####@#@@@@+...:@##=#####====##@@==#=#@:..

...*##==#===##=====####+::+-....*@#@#@@@@@@#@#@*....-+::+####=====###==#==##+..

...*##===#########@:=#@+.........*#@@@@@@@@@@#*.........+@#=:@##########==##*..

...*#=##@@=+::+=@#..:@@@@=.......-#=#@@@@@@###-.......=@@@@:..#@=+::+=@@##=#*..

...+#=@*.............=@@#=--.....=@##******###=.....--=#@@=.............*@=#+..

...:=#-...............=:@-*.....-@@@+......+@@@-.....*-@:=...............-#=:..

...-#..................:-#.-....+@#@:......:@#@+....-.#-:..................#-..

..........................+.....*@@@:......:@@@*.....+.........................

................................+@#@+......+@#@+...............................

................................-@@@#......#@@@-...............................

.................................#@@@-....-@@@#................................

.................................:@@@=....=@@@:................................

...............................:+*@@@@=..#@@@@*+:..............................

...............................*=###==*--*==###=*..............................

    
""")
    cliff_five()
def tree_four():
    tf_app=["A","a","B","b"]
    input_tf=input("You have one of two options:\n"
                   "A. Retreat!!!--But go forward.\n"
                   "B. Do what the cast of Newsies said best and: STRIKE STRIKE STIRKE\n"
                   "STRIKE STRIKE! (aka fight).\n"
                   "")
    if input_tf=="A" or input_tf=="a":
        print("You need to go forward, and somehow, manage to maneuver around the Erymanthian Boar\n"
              "without being seen. You keep pushing forward, and notice a temple in the distance.\n"
              "What do you do?\n"
              "")
        temple()
    elif input_tf=="B" or input_tf=="b":
        print("You choose to fight the boar, what a story this will be for the grandkids!\n"
              "What do you fight with?")
        tree_weapon()
    else:
        tree_four()
def tree_weapon():
    tw_app=["A","a","B","b"]
    input_tw=input("You have one of three options:\n"
                   "A. Use the gun you grabbed from the office.\n"
                   "B. I'm going to fight with my bear hands! I ain't no sissy!\n"
                   "C. Retreat!")
    if input_tw=="A" or input_tw=="a":
        tree_weapon_gun()

    elif input_tw=="B" or input_tw=="b":
        tree_weapon_hand()
    elif input_tw=="C" or input_tw=="c":
        end()
    else:
        tree_weapon()
def tree_weapon_gun():
              
    mHealth=100
    global pHealth
    pHealth=100
    win=0
    choice=input("A. Fight\n"
                 "B. Flee \n"
                 "")
    while choice=="a" or choice=="A":
        pDamage= random.randrange(0,25)
        mDamage= random.randrange(0,25)
        mHealth-= pDamage
        if pDamage==0:
            print("You missed!")
        elif pDamage<=10:
            print("Low damage! You did ", pDamage,"Boar Health is now", mHealth-pDamage)
        elif pDamage>10:
            print("Great damage! You did ", pDamage, mHealth-pDamage)
        if mHealth>0:
            pHealth-=mDamage
            print("The monster is still alive, it hit you for",mDamage, "damage."+
                "Your health is now: ",pHealth-mDamage)
        
        if mHealth<=0:
            print("The monster is dead!")
            win=1
            m_win_tree()
        elif pHealth<=0:
            print("You have died.")
            win=0
            battle_end_boar()
        elif pHealth>=0 or mHealth>=0:
            print("You have", pHealth,"health.")
            print("The monster has", mHealth,"health.")
            fight_again=input("Fight again!:\n"
                              "A. Fight.")
            if fight_again=="A" or fight_again=="a":
                continue
    if choice=="B" or choice=="b":
        print("There is no where to run, you have to fight.")
        tree_weapon_gun()
def tree_weapon_hand():
    mHealth=100
    global pHealth
    pHealth=100
    win=0
    choice=input("Fight or flee!")
    while choice=="a" or choice=="A":
        pDamage=random.randrange(0,10)
        mDamage=random.randrange(0,25)
        mHealth-=pDamage
        if pDamage==0:
            print("You missed!")
        elif pDamage<=10:
            print("Low damage! You did ", pDamage, "Boar Health is now",mHealth-pDamage)
        if mHealth>0:
            pHealth-=mDamage
            print("The monster is still alive, it hit you for:", pHealth-mDamage)
        if mHealth<=0:
            print("The Boar is dead!")
            win=0
            
            m_win_tree()
        elif pHealth<=0:
            print("You have died.")
            win=0
            
            battle_end_boar()
        elif pHealth>=0 or mHealth>=0:
            print("You have", pHealth,"health.")
            print("The monster has", mHealth,"health.")
            fight_again=input("Fight again!:\n"
                              "A. Fight.")
            if fight_again=="A" or fight_again=="a":
                continue
    if choice=="B" or choice=="b":
        print("There is no where to run, you have to fight.")
        tree_weapon_hand()
def battle_end_boar():
    print("You have found valiantly, but alas you have died.\n"
          "Game over.\n")
          
    end()
def m_win_tree():
    global pHealth
    print("You have defeated the Erymanthian Boar! What a feat!\n"
          "The trek, however, is far from over. Your health has\n"
          "been restored.\n"
          "You keep pushing forward, and notice a temple in the\n"
          "distance. You enter the temple.\n"
          "")
    pHealth=100     
    temple()

def cliff_five():
    print("You make it to the end of the tunnel and see a ferocious sight.\n"
          "This bat is as long as a school-bus and tall as a building.\n"
          "It seems to be feeding on something, but stops, smelling the air.\n"
          "What do you do?\n"
          "")
    bat_fight_choice()
def bat_fight_choice():
    bat_app=["A","a","B","b"]
    bat_choice=input("You have one of two options:\n"
                     "A. Fight!\n"
                     "B. Retreat--Find a way around.\n"
                     "")
    if bat_choice=="A" or bat_choice=="a":
          print("With what?")
          bat_weapon()
    elif bat_choice=="B" or bat_choice=="b":
          print("You try to maneuver your way around the bat, but in vain.\n"
                "The bat-god Camazotz turns and decapitates you.\n"
                "You have died.\n"
                "")
          end()
    else:
          bat_choice()
def bat_weapon():
    bw_app=["A","a","B","b"]
    bw_input=input("You have one of three options:\n"
                "A. My bare hands! I'll rip it to shreds!\n"
                "B. The gun my boss gave me!\n"
                "C. Machete.\n"
                "")
    if bw_input=="A" or bw_input=="a":
          bat_weapon_hand()
    elif bw_input=="B" or bw_input=="b":
          bat_weapon_gun()
    elif bw_input=="c" or bw_input=="C":
          print("Sorry, you don't have that or you've already used it.\n"
                "Try again.\n"
                "")
          bat_weapon()
    else:
          bat_weapon()
def bat_weapon_hand():
    bHealth=100
    global pHealth
    pHealth=100
    win=0
    choice=input("Fight or flee!")
    while choice=="a" or choice=="A":
        pDamage=random.randrange(0,10)
        bDamage=random.randrange(0,25)
        bHealth-=pDamage
        if pDamage==0:
            print("You missed!")
        elif pDamage<=10:
            print("Low damage! You did ", pDamage, "Bat Health is now",bHealth-pDamage)
        if bHealth>0:
            pHealth-=mDamage
            print("The monster is still alive, it hit you for:", pHealth-bDamage)
        if bHealth<=0:
            print("The Bat is dead!")
            win=0
            
            m_win_bat()
        elif pHealth<=0:
            print("You have died.")
            win=0
            
            battle_end_bat()
        elif pHealth>=0 or mHealth>=0:
            print("You have", pHealth,"health.")
            print("The monster has", mHealth,"health.")
            fight_again=input("Fight again!:\n"
                              "A. Fight.")
        if fight_again=="A" or fight_again=="a":
            continue
    if choice=="B" or choice=="b":
        print("There is no where to run, you have to fight.")
        bat_weapon_hand()
def battle_end_bat():
    print("Alas, your story has come to an end.\n"
          "You have died. Game over.\n"
          "")
    end()
          
def bat_weapon_gun():
    bHealth=100
    global pHealth
    pHealth=100
    win=0
    choice=input("Fight or flee!")
    while choice=="a" or choice=="A":
        pDamage=random.randrange(0,25)
        bDamage=random.randrange(0,25)
        bHealth-=pDamage
        if pDamage==0:
            print("You missed!")
        elif pDamage<=10:
            print("Low damage! You did ", pDamage, "Bat Health is now",bHealth-pDamage)
        if bHealth>0:
            pHealth-=mDamage
            print("The monster is still alive, it hit you for:", pHealth-bDamage)
        if bHealth<=0:
            print("The Bat is dead!")
            win=0
            
            m_win_bat()
        elif pHealth<=0:
            print("You have died.")
            win=0
            
            battle_end_bat()
        elif pHealth>=0 or mHealth>=0:
            print("You have", pHealth,"health.")
            print("The monster has", mHealth,"health.")
            fight_again=input("Fight again!:\n"
                              "A. Fight.")
        if fight_again=="A" or fight_again=="a":
            continue
    if choice=="B" or choice=="b":
        print("There is no where to run, you have to fight.")
        bat_weapon_gun()
def m_win_bat():
    global pHealth
    pHealth=100
    print("You have defeated the Mayan God Camazotz! Your story now continues.\n"
          "Your health has been restored.\n"
          "You continue down the hallway, realizing this is a temple.\n")
          
    temple()
def temple():
    print("You finally enter a large room with a pedestal in the center\n"
          "It has a misisng piece; a missing rune.\n"
          "What do you do?\n"
          "")
    rune_dec()
def rune_dec():
    global rune
    final_input=input("You have one of two choices:\n"
                      "A. Put the rune in.\n"
                      "B. Try to figure something else out. Indiana Jones-style.\n"
                      "")
    if final_input=="A" and rune==True or final_input=="a" and rune==True:
        print("You place the rune in the empty pedestal.\n"
              ""
              ""
              "")
        win()
    elif final_input=="A" and rune!=True or final_input=="a" and rune!=True:
        print("Sorry, you don't have that with you.\n"
              "")
        partial_win()
    elif final_input=="B" or final_input=="b":
        print("You try to figure something else out, but nothing works.\n"
              "")
        final_input()
    else:
        final_input()
def win():
    print("You have won the game! Congratulations!\n"
          "Would you like to play again?\n"
          ""
          "")
    print(""" __     ______  _    _  __          _______ _   _ 
 \ \   / / __ \| |  | | \ \        / /_   _| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |
    |_|  \____/ \____/      \/  \/   |_____|_| \_|
                                                  
                                                  """)
    end()
def partial_win():
    print("Even though you didn't pick up the rune, you still finished\n"
          "the game. Nice job! Here's a chocolate bar:\n"
          """ _____________,-.___     _
     |____        { {]_]_]   [_]
     |___ `-----.__\ \_]_]_    . `
     |   `-----.____} }]_]_]_   ,
     |_____________/ {_]_]_]_] , `
                   `-'""")
    end()
def end():
    print("You've reached the end of the game. Would you like to\n"
          "play again?")
    end_input=input("A. Yes.\n"
                    "B. No.\n")
    if end_input=="a" or end_input=="A":
        start()
    else:
        print("""_____ _                 _           __                   _             _             _ 
|_   _| |               | |         / _|                 | |           (_)           | |
  | | | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _| |
  | | | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | |
  | | | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| |_|
  \_/ |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, (_)
                                                   | |             __/ |         __/ |  
                                                   |_|            |___/         |___/   """)
    

        

    
    
        
        
        
        
start()
                    
