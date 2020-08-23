print("Hello I am a Robot")
print('o------ RO')
print('  ||||  BOT')
#name = input("\n Please may I know your name? ")

#print("\n Welcome " + name + " !")

#color = input("\n What is your favorite color? ")
#print(name + " likes " + color + ".")

#weight = input("\nWhat is your weight in lbs? ")
#weight_Kg = int(weight) * 0.45
#print("You weigh " + str(weight_Kg) + " in Kg. ")
#print("Now let's get down to business \n")

print('>>Choose "y" for yes and "n" for No in the next question \n')
q1 = input('Do you desire to get loan from Feomasix Investment? ')
while True:
    if q1 == 'y':
        print("Please Proceed to the next question\n")

    elif q1 == 'n':
        print("you're in the wrong place.\n")
        break
    else:
        print('Invalid input \n')
        break

    #print('>>The following question is crucial for your loan collection \n')
    #print('Answer the Questions Honestly \n')

    #print(">> Please write in figures only. Don't use comma(,) in between digits \n")
    q2 = int(input('How much is your annual income? \n'))
    if q2 >= 1000000:
        print('>>Please Proceed to the next question \n')
        break
    elif q2 < 1000000:
        print('>> Sorry! You are not Eligible for our loan scheme \n')
        break
    else:
        print('Invalid input \n')
        break

    q3 = int(input("How much did you want to loan? "))
    if q3 == int(_):
        print("Congratulations You've got a loan! ")
