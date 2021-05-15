
from random import choice
lss = list(range(0,10))
print("The Name of the Game is Bulls and Cows")
print("You have to guess a four digit number from 0000 to 9999(both inclusive)")
print("If a digit of your guessed number is on the same position as the random number then you will have a Bull")
print("If a digit of your guessed number is in the random number but on a different position then you get a Cow")
print("Try to find out how many tries it takes you")
print("To make it easy, all the digits are distinct")   
def num_generator():
    nn = choice(lss)    
    lss.remove(nn)
    return nn

def initialize():
    numbers = []
    for i in range(4):
        num = num_generator()
        numbers.append(num)
    return numbers
    
def user_input():
    user_num = input("Enter Number: ")
    if user_num == "quit":
        return user_num
    user_numbers = [int(i) for i in user_num]
    return user_numbers

def game():
    computer = initialize()
    user = user_input()
    tries = 0
    while computer != user:
        if(user == "quit"):
            print(computer)
            break;
        bulls = 0
        cows = 0
        pos1 = 0
        for a in computer:
            pos2 = 0
            for b in user:
                if(b==a):
                    if(pos1==pos2):
                        bulls +=1
                    else:
                        cows += 1
                pos2 += 1
            pos1 +=1
        print("Bulls: ", bulls)
        print("Cows: ",cows)
        user = user_input()
        tries += 1
    if(user == computer):
        print("Congratulations on guessing the number!")
        print("It took you", tries, "tries")

game()