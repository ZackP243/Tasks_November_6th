import math
running=0

driver_speed= int(input("The speed limit is 50Km/h how fast are you driving"))

if driver_speed == 50: #Checks if the input number is 50
    print("You are right on the speed limit pal")
elif driver_speed < 50:#Checks if the input number is lower than 35
    print ("You are going a little slow might want to speed up")
elif driver_speed  <70: #Checks if the input number is lower than 70 but only after it checks if it is lower than 35
    print("Slow down there bucko you're moving to quick you have to pay $45")
elif driver_speed >= 80:#Checks if the input number is higher than 80 only after the code above it has been checked
    print("SLOW DOWN you have to pay $150")
elif driver_speed >= 75: #Checks if the input number is greater than 75
    print("Holy Moly you're moving quick slow down you have to pay $75")


win_counter = 0
for x in range(0,6):#Makes it repeat the question 6 times
    counter_input = input("Did you win or lose your match")

    if counter_input == ("w"):
        win_counter = win_counter + 1#makes it increase by 1 every time w is pressed

if win_counter == 1 or win_counter == 2:#Checks what the win counter is and puts person in a group
    print("You are in group 3")
if win_counter == 3 or win_counter == 4:#Checks what the win counter is and puts person in a group
    print("You are in group 2")
if win_counter == 5 or win_counter == 6:#Checks what the win counter is and puts person in a group
    print("You are in group 1")


if win_counter == 0:#Checks what the win counter is and puts person in a group
    print("You are eliminated")
mark = 0

number_course =int(input ("How many courses did you take"))
for x in range(0,number_course,):#Makes it repeat the question based on the number put into the initial question
    input_number=int(input("What was your mark in the course."))
    mark = (mark+input_number)#adds the mark and the numbers you put in
mark = (mark/number_course)# divides the mark by the numbers you inputted
if mark >= 79.5:
    print("Nice job you got the principals award")
elif mark < 79.5:
    print("OOOOOOOOf you didn't get the principal's award")


money=0
cookie=int(input("How many cookies are being produced"))#asks how many cookies are being produced
if cookie<=200:
    print("That's an invalid amount of cookies")#if it is under 200 says that that is invalid

crates=int(cookie/(12*20))
money=money+crates*80
cookie=int(cookie-crates/(12*20))
boxes=int(cookie/12)
money=money+boxes*5
cookie=int(cookie-boxes*12)
print(crates,"crates",boxes,"boxes",cookie,"cookies")
print("It will cost",(money),"$")


start=int(input("Choose 1 2 or 3 or 4 to restart"))#tells you how to begin
if start == 1: # this all calculates the pythagoras of a triangle with two side lengths given
     pythagoras=0
     for x in range(0,2):
        pythagoras_input=int(input("What is one of your two numbers"))
        pythagoras=(pythagoras_input*pythagoras_input+pythagoras)
     pythagoras = math.sqrt(pythagoras)
     print("Side Length =",pythagoras)
if start == 2:
     tip=0 #This calculates how much tip you should give for a certain percentage for a certain price
     bill_input=int(input("How much was the bill?"))
     percent_input=int(input("What percent do you want to tip?"))
     percent_input=percent_input/100
     print("you will need to tip" + str(percent_input*bill_input)+"$")
if start == 3: #this all converts farenheight to Celsius
     temp_input=int(input("What is the temperature"))
     temp_check=str(input("Is you temperature in Celsius or Fahrenheit"))
     if temp_check == ("celsius"):
        print("The temperature is "+ str(temp_input * 9/5 + 32) + "in Fahrenheit")
     elif temp_check == ("fahrenheit"):
            print("the temperature is "+str(temp_input - 32 * 5/9) + "in Celsius")


