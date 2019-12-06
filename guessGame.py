

# this is a Guest Game for pratice while loop skill

secretNumber = 9
countLimit = 3
countTimes = 0

while countTimes < countLimit:
    guestNaumber = int(input('Guess: '))
    countTimes += 1
    if guestNaumber == secretNumber:
        print('you win!')
        break
else:
    print('you lose!! LOL!')
# print('you lose!!!')
