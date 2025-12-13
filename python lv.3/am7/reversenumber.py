high = 100
low = 1
guesses = 0
while True:
    mid = (low+high)//2
    if guesses == 6:
        print(f'your number was {mid}! I knew I would get it. :)')
        break
    
    elif low == high:
        print(f'your number was {high-low+high}! >:)')
        break
    
    inpt = input(f'is this your number:{mid} \n yes) \n lower) \n higher) \n :')

    if inpt == "yes":
        print("haha I knew I would guess your number. :)")
        break

    elif inpt == "lower":
        high = mid-1

    elif inpt == "higher":
        low = mid+1

    else:
        print("error please try again.")
        guesses -= 1

    guesses += 1


print()