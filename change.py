#Kyla Ryan
#9/21

#change sorter

def change():
    #1 get amount of change from user; the input
    total_change=int(input("How much change do you have in your pocket? "))
    #2 calc total for q n d p
    quarters=total_change // 25
    whats_left=total_change % 25
    dimes=whats_left // 10
    whats_left=whats_left % 10
    nickles=whats_left // 5
    whats_left=whats_left % 5
    pennies=whats_left
    #3 display back to user
    print("Quarters:",quarters, "\nDimes:",dimes, "\nNickles:",nickles, "\nPennies:",pennies)
change()

def change2(total_change):
     #1 get amount of change from user; the input.
    
    total_change=total_change
    #2 calc total for q n d p
    quarters=total_change // 25
    whats_left=total_change % 25
    dimes=whats_left // 10
    whats_left=whats_left % 10
    nickles=whats_left // 5
    whats_left=whats_left % 5
    #Asign a variable to each calculation, updating what the variable is each time.
    pennies=whats_left
    #3 return value
    return quarters, dimes, nickles, pennies
#Ask for the total number of change in the person's pocket.
#Call the function, assigning strings to the amounts given. 
total_change=int(input("how much change do you have in your pocket? "))
quarters, dimes, nickles, pennies = change2(total_change)
print("Quarters:",quarters, "\nDimes:",dimes, "\nNickles:",nickles, "\nPennies:",pennies)


#Import python functions.
import calendar
import time
#Define the function, using GMT time.
def gmt():
    print("TIME:")
    #figure the ms s m h. Assign variables to calculations to deterime hours, minutes, seconds
    #Each calculation is divided by 60, except for hours (by 24)

    totalSeconds=calendar.timegm(time.gmtime())
    current_seconds=totalSeconds % 60
    totalMinutes=totalSeconds//60
    current_minutes=totalMinutes % 60
    totalHour=totalMinutes//60
    current_hour=totalHour % 24
    #return totalHour, totalMinutes, totalSeconds
    return current_hour, current_minutes ,current_seconds
    #Loop the function to give an updated time each second. 
x=True
while x==True:
    h,m,s=gmt()
    print(h,":",m,":",s)
