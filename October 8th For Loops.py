print ("Hello World")
ex_var = 32
ex_var2 = ("Hi")
user_input = int(input ("Give me some input"))
if user_input ==3:
    print("Your input was 3")
elif user_input %2 == 0:
    print("Your input was even")
else:
    print("your number is not 3 or even")

counter=0
while counter < 100:
    print(counter)
    counter=counter + 20

for x in range(10,0,2):
    print("five")
    print(x)
for x in range(0,14):
    print(x)
for x in range(100,600,27):
    print(x)
ask_input = int(input("Pick an number"))

print ("are we there yet\n" * ask_input)
average_input = 0
for x in range(0,8):
    average_input=int(input("Input you mark"))+average_input
print(average_input/8)

