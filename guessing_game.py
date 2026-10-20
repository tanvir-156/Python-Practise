import random
def play_game():
    lucky_num = random.rnadint(1, 50)

    while True:
        user_num= int(input("Guess the lucky number: "))
        if user_num== lucky_num:
            print("You won. game over!!")
            break
        elif user_num<lucky_num:
            print("Too Low")
        else:
            print("Too High")

print("Thank you for playing")