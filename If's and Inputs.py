Birthday=input("When is your Birthday")
Birthmonth= input("When is your Birthmonth")
BirthYear= input("When is your birth year")

user_name= input("What is your name")
print ("hello"+user_name)
if 4<3:
    print ("4 is more than 3")
number=int(input("Pick a number"))
if number > 10:
    print ("that number is greater")
if number < 10:
    print ("That number is less than 10")

input_word=str(input("Pick a word"))
if len(input_word) <5:
    print ("This word has less than 5 letters")
if len(input_word) > 5:
    print ("This word has more than 5 letters")
if len(input_word) == 5:
    print ("this word has 5 letters")

input_course1=int(input ("What mark did you get in Science"))
input_course2= int(input ("What mark did you get in Math"))
input_course3= int (input ("What mark did you get in History"))
input_course4= int(input ("What mark did you get in English"))
if ((input_course1) + (input_course2) + (input_course3) + (input_course4))/4 >80:
    print("Nice job you got over 80")
if ((input_course1) + (input_course2) + (input_course3) + (input_course4))/4 <50:
    print ("uh oh you got under a 50")