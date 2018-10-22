#Kyla Ryan 
#9/18
#Get Name Function

#Import math functions
import math
#define function to ask user for name input
def get_name():
    name=input("What is your name? ")


#display name
    print("The name you entered was", name)





print("This is our function")
#get_name()


#define function for area of a circle. Assign variables to functions for calculations.
def areaOfCircle(radius1):
    PI = 3.14159263
#1 Get a radius
    radius = radius1
    
    
#2 compute an area. Area is r^2*Pi
    radius = float(radius)
    area = radius*radius*PI
#3 Display informaiton back
    print("The area of the circle is: ",area)
inputx("What is radius? ")
areaOfCircle(radiusx)

#Assign function for pythagorean theorum
def pythagorean_theorum_1():
    #a^2+b^2=c^2
    #Ask for the sides of the triangle to compute
    a=float(input("what is side a of the triangle?"))
    b=float(input("what is side b of the triangle?"))
    c=a*a+b*b #Assign c as the first side squared, plus, the second side squared. 
    
    print("The third side is",c)
#Present the calculation to the user and call the function. 
pythagorean_theorum_1()

#Assign function again, but give parameters.
def pythagorean_theorum(ax,bx):
    #a^2+b^2=c^2
    a=float(ax)
    b=float(bx)
    c=a*a+b*b
    #Assign a mathematic equation to the c value to calculate the side of the hypoteneus squared.
    #Then take the square root by calling the math.sqrt function of c to find the side. 
    c=math.sqrt(c)
    
    print("The third side is",c)
#Assign variables to the user's inputs for the trangle sides.
ax=input("what is side a of the triangle?")
bx=input("what is side b of the triangle?")
pythagorean_theorum(ax,bx)

#Define the function to add two numbers together
#Ask for inputs from the user.
#Create a function to add the two assigned variables together.
#Assign a variable to the equation to simplify the function for better output.
#Call the function by the variable.

def add_numbers():
    num1=input("enter a number")
    num2=input("enter a second number")
    num3=int(num1)+int(num2)
    return num3
num4=add_numbers() #num4=num3
print("the sum of your numbers is: ",num4)

print(num4)
add_numbers()
#Do the same function as the Add Numbers, but assign variables to the input numbers.
def add_numbers(X,Y):
    num1=X
    num2=Y
    num3=int(num1)+int(num2)
    print("this is num1")
    print("this is num2")
    return num3
X=input("enter a number")
Y=input("enter a second number")
num4=add_numbers(X,Y) #num4=num3
print("the sum of your numbers is: ",num4)

print(num4)

#Define the function for the user's name. 
def get_name(name_input):
    


#display name
   name=name_input
   name.lower()
   name=name.title()
   print("the name you entered was",name)
   print("is this correct? yes or no")



print("This is our function")
name=input("what is your name")
get_name(name)


