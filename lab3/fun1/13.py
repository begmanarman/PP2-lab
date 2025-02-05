from random import randint

def play():
    num = randint(1,20)
    print("hello ! what is your name?")
    name =input()
    print(f"Well , {name} ,  I am thinking of a number between 1 and 20.")
    x=True
    z=0
    while x :
        number = int(input("Take a guess."))
        z +=1
        if number==num :
            print(f"Good job, KBTU! You guessed my number in {z} guesses!")
            x=False
            break
        if number > num :
            print("Your guess is too high.")
        if number < num:
            print("Your guess is too low")

play()


