import random
import re

'''
word guess game
This could be written a bit more efficient but its functional
I may revisit this in the future to make it maybe use Pygame but we will see
'''


def getWord():
    with open("wordlist.txt", "r") as f:
        lines = f.read().splitlines()
        f.close()
        return random.choice(lines)
def displayWord(word, cGuess ):
    res = ""
    if len(cGuess) >0:
        for letter in word:
            res += letter if letter in cGuess else '*'
        return res
    else:
        for i in word:
            res += "*"
        return res

def checkInput(st):
        check_string = re.compile("[^a-zA-Z]")
        if check_string.search(st) == None:
            return False
        else:
            return True


def main():
    word = getWord().upper()
    wrongGuesses = [] #what they guess so far
    correctGusses = [] #whats write 
    numGuess = len(word)+2 #give them some more guesses 
    print("hello and welcome to word guess!\n The word has: "+ str(len(word))+ " letters and you have " + str(numGuess)+ " guesses\n if you wish to quit type quit at anytime! \n Good Luck!" )
    hide = displayWord(word, correctGusses)
    while True:
        print("Hidden word: "+ hide )
        if len(wrongGuesses) > 0:
            st = ""
            for wrong in wrongGuesses:
                st += ","+ wrong
            print("wrong guesses: " + st  )
        else:
            print("no wrong guess yet!")
        print("word length: " + str(len(word)))
        print("Geusses Left: " + str(numGuess) )
        guess = input("Enter letter >> ").upper()
        if checkInput(guess) == True:
            print("Please enter letters only!")
            continue
        elif guess in wrongGuesses:
            print("You guess that alerady!")
            continue
        elif guess =="QUIT":
            print("Thanks for playing!")
            break
        if guess in word:
            correctGusses.append(guess)
            hide = displayWord(word,correctGusses)
            print("Hidden word: " + hide )
        else:
            wrongGuesses.append(guess)
            numGuess -= 1 
            print("Sorry incorrect! Number of guesses left: " + str(numGuess))
            
        if hide == word and numGuess != 0:
            print("Well done you got the word with: " +str(numGuess) + " number of gesses left")
            break
        elif numGuess == 0:
            print("sorry you are out of guesses the  word was: " + word )
            break


    



        


if __name__ == "__main__":
    main()