current_date="October 31st"
if current_date=="October 31st":
    print ("it is Halloween!")
elif current_month=="October":
    print("It is October")
else:
    print('it is not halloween')

write_check = 0
while write_check <5:
    print("Hello")
    write_check = write_check + 1

number_check=-1
while number_check < 20:
    print (number_check +1 )
    number_check=number_check+1

number_check=0
while number_check < 20:
    print (number_check +2 )
    number_check=number_check+2


x_year=1967
input_year = int(input("What year will the leafs win"))

while x_year != input_year:
    print("Leafs did not win in" + str(x_year) + "but they will win in" + str(input_year) + ".")
    x_year = x_year+1

number = int(input("pick a number"))
number = number - 1
while number != 0:
    print(number - 1)

