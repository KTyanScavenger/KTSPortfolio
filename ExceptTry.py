#Kyla Ryan
#1/19

while True:
    try:
        num=float(input("Enter a number: "))
        break
    except ValueError:
         print("You must enter a number. ")
    except TypeError:
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

try:
    num=float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number! Or as python would say...")
    print(e)
try:
    num=float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)
