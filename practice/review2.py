import random
'''
note the env that this was wrtine in was 3.5 not 3.6+ hence no f"" for string formating
This is a combination of rebiewing a few things 
-string manuplation 
-shuffle and deal cards out
-rolling dice

'''
def deal(list):
    players = []
    i = 1
    while i <= 4:
        temp = []
        for card in range(0,6):
            val = list.pop(card)
            temp.append( val )
        players.append(temp)
        i += 1
    return players

def card():
    list = ["A" ,"K", "Q",  "J", 2,3,4,5,6,7,8,9,10]
    suite = ["h", "d", "s", "c"]
    deck = []
    for x in suite:
        for card in list:
            newcard = str(card) + ":" + x 
            deck.append(newcard)
    uIn = input("type y if you want to shuffle: ")
    if uIn != "y":
        tempDeck = deal(deck)
        print("yours hands are ")
        for hand in tempDeck:
            print(hand)
    else:
        random.shuffle(deck)
        hands = deal(deck)
        print("yours hand are")
        for hand in hands:
            print(hand)


def diceUser():
    val = input("Eneter how many sides and dice you would like in format numsidednumdice ex: 6D8 >> ")
    list = val.split("d")
    return list

def diceRoll(num):
    ran = random.randint(1,num+1)
    return ran

def dice():
    list = diceUser()
    numDice = int(list[1])
    numSides = int(list[0])
    total = 0
    for i in range(1,numDice+1):
        num = diceRoll(numSides)
        total += num
        print("you rolled dice: " + str(i)+ ": " + str(num))
    print("total: " + str(total))


'''
def timeStuff():
    val = input("Enter HH:MM: ")
    list = val.split(":")
    hour = int(list[0])
    min = int(list[1])
    totalmin = min + (hour * 60)
    totalsec = totalmin * 60
    pint("total seconds: "+ str(totalsec))
    print("total min: " + str(totalmin)
'''
if __name__ == "__main__":
    card()
    dice()