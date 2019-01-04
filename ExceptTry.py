#Kyla Ryan
#1/19
##Try to give erors without the actual error
while True:
    try:
        #Ask for a number from the user
        num=float(input("Enter a number: "))
        break
    except ValueError:
        #This gives the exception of a character that is not a number. 
         print("You must enter a number. ")
    except TypeError:
        #Incorrect input somewhere
        print("Something went wrong.")
print(num)
for value in (None,"Hi!"):
    try:
        print("Attempting to convert",value,"-->",end="")
        print(float(value))
    except ValueError:
        print("You must enter a number")
    except TypeError:
        print("Something went wrong.")
#The previous code attempts to convert the value into floats. 
try:
    num=float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number! Or as python would say...")
    print(e)
    #This allows the user to see the actual error with a simplified version. 
try:
    num=float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)
