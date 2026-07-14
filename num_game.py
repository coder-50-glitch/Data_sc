import random
play = True
no = int(random.randint(1,9))
print(no)
print("i will generate a no bet 10 to 20 n u hv to guess a no at a time")
print("the game end if u get 1 !")
while play:
    guess = int(input("u r best guess"))
    if(no == guess):
        print("u win \n the no is ", no)
        break
    else:
        ("Wrong guess try again ")
        