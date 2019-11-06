attack1=str
import random
import time
health=0
bhealth=0
chealth=0
shealth=0
pokemon = str()
name=str(input("Hi there adventurer what is you're name"))
ask=str(input("\nHi "+ name + " are you ready to begin you're pokemon adventure!"))
if ask == "no"or ask =="No":
    print("Ok bye bye.")
    quit
if ask == "yes" or ask == "Yes" or ask == "ya" or ask == "Ya"or ask ==" Yes" or ask == " yes" or ask == " ya":
    pokemon=str(input("What pokemon do you want \n\nCharmander \n\nBulbasaur \n\nSquirtle."))
else:
    ask == "yes" or ask == "Yes" or ask == "ya" or ask == "Ya" or ask == " Yes" or ask == " yes" or ask == " ya"


if pokemon == "Squirtle":
    print("\nNice you picked "+ pokemon)
    rival=str(input("What is your rival's name"))
    print("\nCool his name is" + rival)
    rival_pokemon=str(input("oops I forgot what pokemon he picked. Can you tell me which one"))
    while rival_pokemon == pokemon:
        rival_pokemon = str(input("Wait no thats yours. What's his"))
    print("\n Uh oh he's challenged you to a battle")
    print(rival + " deploys " + rival_pokemon)
    print("\n" + name +" deploys" + pokemon)
    resource = 0
    resource=(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
    if resource == "1":
        attack1=str(input("What attack do you want to use tackle or Bubble"))
        resource = 0
    if resource == 2:
        print("you have nothing in your bag")
        resource = int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
        resource = 0
    if resource == 3:
        print("you can't run from " + rival)
        resource = int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
        resource = 0
    if attack1 == "tackle" or attack1== "Tackle":
        if rival_pokemon == "Charmander":
            print("Squirtle used " + attack1)
            print("it did 15/50 damage")
            chealth = 35
            print(rival_pokemon + " used flame")
            print("it was a critical hit it did 50/50 damage")
            health=0
        if health== 0:
            print("your pokemon fainted you were taken to the nearest pokecentre")
    if attack1 == "Bubble":
        print("squirtle used " + attack1)
        if rival_pokemon=="Charmander":
            print("It's super effective")
            print("it did 45/50 damage")
            chealth=5
            print(rival_pokemon + " used flame")
            print("it's not very effective it only did 20/50 damage")
            health=30
            attack2=str(input("Will you use tackle or Bubble"))
            if attack2 == "tackle" or attack2 == "bubble" or attack2 == "Bubble" or attack2 == "Tackle":
                print(rival_pokemon + " fainted")
        if attack1 == "tackle" or attack1 == "Tackle":
            if rival_pokemon == "Bulbasaur":
                print("Squirtle used " + attack1)
                print("it did 15/50 damage")
                bhealth = 35
                print(rival_pokemon + " used Leaf sweep")
                print("it was a critical hit it did 50/50 damage")
                health = 0
            if health == 0:
                print("your pokemon fainted you were taken to the nearest pokecentre")
        if rival_pokemon == "Bulbasaur":
            print("it's not very effective it did 10/50 damage")
            bhealth=40
            print(rival_pokemon + " used Leaf sweep")
            print("it's super effective")
            print("it did 45/50 damage")
            health=5
            attack2 = str(input("Will you use tackle or leaf sweep"))
            if attack2 == "tackle" or attack2 == "bubble" or attack2 == "Bubble" or attack2 == "Tackle":
                print("that dealt 15")
                bhealth=25
                print(rival_pokemon + (" Used tackle"))
                print("Your pokemon fainted you were taken to the nearest pokecentre")
if pokemon == "Charmander":
    print("\nNice you picked "+ pokemon)
    rival=str(input("What is your rival's name"))
    print("\nCool his name is" + rival)
    rival_pokemon=str(input("oops I forgot what pokemon he picked. Can you tell me which one"))
    while rival_pokemon == pokemon:
        rival_pokemon = str(input("Wait no thats yours. What's his"))
    print("\n Uh oh he's challenged you to a battle")
    print(rival + " deploys " + rival_pokemon)
    print("\n" + name +" deploys" + pokemon)
    resource=int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
    resource = 0
    if resource == 1:
        attack2=str(input("What attack do you want to use Tackle or Flame"))
    if resource == 2:
        print("you have nothing in your bag")
        resource = int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
    if resource == 3:
        print("you can't run from " + rival)
        resource = int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
    if attack2 == "tackle" or attack2== "Tackle":
        if rival_pokemon == "Bulbasaur":
            print("Charmander used " + attack2)
            print("it did 15/50 damage")
            chealth = 35
            print(rival_pokemon + " used flame")
            print("it was a critical hit it did 50/50 damage")
            health=0
        if health== 0:
            print("your pokemon fainted you were taken to the nearest pokecentre")
    if attack2 == "Flame":
        print("Charmander used flame")
        if rival_pokemon=="Bulbasaur":
            print("It's super effective")
            print("it did 45/50 damage")
            bhealth=5
            print(rival_pokemon + " used Leaf Sweep")
            print("it's not very effective it only did 10/50 damage")
            health=40
            attack2 = str(input("Will you use tackle or Flame"))
            if attack2 == "tackle" or attack2 == "flame" or attack2 == "Flame" or attack2 == "Tackle":
                print(rival_pokemon + " fainted")
        if attack2 == "tackle" or attack2 == "Tackle":
            if rival_pokemon == "Squirtle":
                print("Bulbasaur used " + attack2)
                print("it did 15/50 damage")
                shealth = 35
                print(rival_pokemon + " used bubble")
                print("it was a critical hit it did 50/50 damage")
                health = 0
            if health == 0:
                print("your pokemon fainted you were taken to the nearest pokecentre")
        if rival_pokemon == "Squirtle":
            print("print it's not very effective it did 10/50 damage")
            print(rival_pokemon + " used Bubble")
            shealth=40
            print("it's super effective")
            print("it did 45/50 damage")
            health=5
            attack2 = str(input("Will you use tackle or Flame"))
            if attack2 == "tackle" or attack2 == "flame" or attack2 == "Flame" or attack2 == "Tackle":
                print("that dealt 15 damage")
                bhealth = 25
                print(rival_pokemon + (" Used tackle"))
                print("Your pokemon fainted you were taken to the nearest pokecentre")
if pokemon == "Bulbasaur":
    print("\nNice you picked "+ pokemon)
    rival=str(input("What is your rival's name"))
    print("\nCool his name is" + rival)
    rival_pokemon=str(input("oops I forgot what pokemon he picked. Can you tell me which one"))

    print("\n Uh oh he's challenged you to a battle")
    print(rival + " deploys " + rival_pokemon)
    print("\n" + name +" deploys" + pokemon)
    resource=int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
    resource = 0

    if resource == 1:
        attack1=str(input("What attack do you want to use tackle or Leaf sweep"))
        resource=0
    if resource == 2:
        print("you have nothing in your bag")
        resource = int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
        resource=0
    if resource == 3:
        print("you can't run from a proffesional battle")
        resource = int(input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
        resource=0
    if attack1 == "tackle" or attack1== "Tackle":
        if rival_pokemon == "Squirtle":
            print("Bulbasaur used " + attack1)
            print("it did 15/50 damage")
            bhealth = 35
            print(rival_pokemon + " used bubble")
            print("it was a critical hit it did 50/50 damage")
            health=0
        if health== 0:
            print("your pokemon fainted you were taken to the nearest pokecentre")
    if attack1 == "Leaf sweep":
        print("Bulbasaur used " + attack1)
        if rival_pokemon=="Squirtle":
            print("It's super effective")
            print("it did 45/50 damage")
            shealth=5
            print(rival_pokemon + " used flame")
            print("it's not very effective it only did 10/50 damage")
            health=40
            attack2=str(input("Will you use tackle or leaf sweep"))
            if attack2 == "tackle" or attack2 == "Tackle":
                print(pokemon + " used tackle it did 15 damage")
                shealth=0
            if attack2 == "leaf sweep" or attack2 == "Leaf sweep":
                print(pokemon + " used leaf sweep it did 15 damage")
                shealth=0
            if shealth==0 or shealth < 1:
                print(rival_pokemon + " was defeated " + rival + " runs awy with his injured pokemon")
        if rival_pokemon == "Charmander":
            print("it's not very effective it did 10/50 damage")
            print(rival_pokemon + " used flame")
            chealth=40
            print("it's super effective")
            print("it did 45/50 damage")
            health=5
            attack2 = str(input("Will you use tackle or leaf sweep"))
            if attack2 == "tackle" or attack2 == "leaf sweep" or attack2 == "Leaf sweep" or attack2 == "Tackle":
                print("that dealt 15")
                chealth = 25
                print(rival_pokemon + (" Used tackle"))
                print("Your pokemon fainted you were taken to the nearest pokecentre")
else:
    pokemon = str(input("What pokemon do you want \n\nCharmander \n\nBulbasaur \n\nSquirtle."))

time.sleep(5)
print("you are ready to begin you're adventure you can now leave pallat town and begin on route 1")
time.sleep(1)
print("You have come to a cross roads will you turn left or right")
path_choice = random.randint(1, 2)
if path_choice==1:
    print ("a bird distracts you and you turn left")
    print("you meet a man who tells you about the ultimate pokemon tournament and you are raring to participate")
if path_choice == 2:
    print("You decide to turn right after seeing a squirrel run that way")
    pokemon1 = random.randint(1,10)
    if pokemon1 == 3:
        print("you were running along the path when you found a pidgey ")
        pokemon_catch=str(input(":would you like to catch the pidgey"))
        if pokemon_catch == "yes":
            print("nice you through a pokeball and caught the pidgey")
        if pokemon_catch == "no" or pokemon_catch == "No" or pokemon_catch == " no":
            print("Ok pokemon escaped")
print("Your Pokemon's evolving!!")
time.sleep(3)
if pokemon == "Charmander":
    print(pokemon + " turned into a Charmeleon")
if pokemon == "Squirtle":
    print(pokemon + " turned into a Wartortle")
if pokemon == "Bulbasaur":
    print(pokemon + " turned into a Ivysaur")
print("You have come to a large forest you need to escape!")
for x in range (0,10):
    maze=int(input("press 1 for left and 2 for right"))
if maze == 15:
    print("You got out of the forest")
print("for completing the forest you got a max potion")
print(str(pokemon) + " is pretty weak would you like to use the max potion on it")
potion=str(input("Press 1 for yes press 2 for no"))
if potion == "1":
    print("ok " + pokemon + " is at full health")
if potion == "2":
    print("ok")
time.sleep(3)
print("\n you have come across the final pokemon battle")
print("You go in and find yourself in a course")
log=input("you come across a log press 1 to jump over press 2 to slide under")
if log == "1":
    print("you jumped over safely")
    river=input("you see a river that you have to cross press 1 to swim through press 2 to jump over")
    if river == "1":
        print("you swam through and safely got to the other side")
        print("You come out of the river to see the gym leader Brock")
        print("you challenge him to a battle")
        print(name + " deploys " + pokemon)
        print("Brock deploys Onix")
        resource = (input("Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
        if resource == "1":
            if pokemon == "Squirtle":
                attack4 = str(input("What attack do you want to use tackle or Bubble"))
            if pokemon == "Charmander":
                attack4 = str(input("What attack do you want to use tackle or Flame"))
            if pokemon == "Bulbasaur":
                attack4 = str(input("What attack do you want to use tackle or Leaf Sweep"))
            resource = 0
        if resource == "2":
            print("you have nothing in your bag")
            resource = int(input(
                "Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
            resource = 0
        if resource == "3":
            print("you can't run from " + rival)
            resource = int(input(
                "Do you want to attack check your bag or run. For attack press 1 For bag press 2 For run press 3"))
            resource = 0
        if attack4 == "Flame":
            print(pokemon + " used Flame")
            print("it did 20/50 damage")
            print("Onix used rock slide")
            print("it did 20/50 damage")
            attack4=str
            if pokemon == "Squirtle":
                attack5 = str(input("What attack do you want to use tackle or Bubble"))
            if pokemon == "Charmander":
                attack5 = str(input("What attack do you want to use tackle or Flame"))
            if pokemon == "Bulbasaur":
                attack5 = str(input("What attack do you want to use tackle or Leaf Sweep"))
        if attack4 == "Leaf Sweep":
            print(pokemon + " used Leaf Sweep")
            print("it did 20/50 damage")
            print("Onix used rock slide")
            print("it did 20/50 damage")
            attack6 = str
            if pokemon == "Squirtle":
                attack6 = str(input("What attack do you want to use tackle or Bubble"))
            if pokemon == "Charmander":
                attack6 = str(input("What attack do you want to use tackle or Flame"))
            if pokemon == "Bulbasaur":
                attack6 = str(input("What attack do you want to use tackle or Leaf Sweep"))
        if attack4 == "Bubble":
            print(pokemon + " used Bubble")
            print("it's super effective")
            print("it did 35/50 damage")
            print("Onix used rock slide")
            print("it did 20/50 damage")
            if pokemon == "Squirtle":
                attack7 = str(input("What attack do you want to use tackle or Bubble"))
            if pokemon == "Charmander":
                attack7 = str(input("What attack do you want to use tackle or Flame"))
            if pokemon == "Bulbasaur":
                attack7 = str(input("What attack do you want to use tackle or Leaf Sweep"))
        if attack4 == "Tackle":
            print("it did 20/50 damage")
            print(pokemon + " used Tackle")
            print("Onix used rock slide")
            print("it did 20/50 damage")
        attack8 = str
        if pokemon == "Squirtle":
                attack8 = str(input("What attack do you want to use tackle or Bubble"))
        if pokemon == "Charmander":
            attack8 = str(input("What attack do you want to use tackle or Flame"))
        if pokemon == "Bulbasaur":
            attack8 = str(input("What attack do you want to use tackle or Leaf Sweep"))
        if attack8 == "Bubble":
            print(pokemon + " used Bubble")
            print("it's super effective it did 50/50 damage")
        if attack8 == "Flame":
            print(pokemon + " used Flame")
            print("Critical hit it did 50/50 damage")
        if attack8 == "Leaf sweep":
            print(pokemon + " used Leaf sweep")
            print("Critical hit it did 50/50 damage")
        if attack8 == "Tackle":
            print("Critical hit it did 50/50 damage")
        print("YOU WIN!!!!! GREAT JOB!!!!!")
