import random

def get_word():
    '''Returns random word.'''
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def check(word,guesses):
    '''Creates and returns string representation of word

    displaying asterisks for letters not yet guessed.'''
    status = '' #Current status of guess
    last_guess = guesses[-1]
    matches = 0 #Number of occurences of last_guess in word
    print(word)
    for letter in word:
        if letter == last_guess:
            matches += 1 
            status += letter
        else:
            status += "#"
    if matches > 1 :
        print("there were " + str(matches) + " many matches for" + last_guess + " your guess" )
    elif matches == 1:
        print("there was one " + last_guess)
    else:
        print("sorry no matches")
        

    #Loop through word checking if each letter is in guesses
    #  If it is, append the letter to status
    #  If it is not, append an asterisk (*) to status
    #Also, each time a letter in word matches the last guess,
    #  increment matches by 1.

    #Write a condition that outputs one of the following when
    #  the user's last guess was "A":
    #   'The word has 2 "A"s.' (where 2 is the number of matches)
    #   'The word has one "A".'
    #   'Sorry. The word has no "A"s.'

    return status

def main():
    word = get_word() #the random word
    n = len(word) #the number of letters in the random word
    guesses = [] #the list of guesses made so far
    guessed = False
    print('The word contains {} letters.'.format(n))
    word = word.lower()
    while not guessed:
        print("type quit at any time to exit the app!")
        guess = input('Guess a letter or a {}-letter word: '.format(n))
        guess = guess.lower()
        if guess.upper() == "QUIT":
            print("Goodbye!")
            break
        if len(guess) > 1 and len(guess) == len(word):
            if word == guess:
                guessed = True
                guesses.append(guess)
                continue
            else:
                print("not correct try again")
        elif guess in guesses:
            print("you guessed that already")
            guesses.append(guess)
            continue
        elif len(guess) == 1:
            guesses.append(guess)
            res = check(word, guesses)
            print("word: " + res)
            continue
        else:
            guesses.append(guess)
            print("invalid input try again")
            continue
        #Write an if condition to complete this loop.
        #You must set guessed to True if the word is guessed.
        #Things to be looking for:
        #  - Did the user already guess this guess?
        #  - Is the user guessing the whole word?
        #     - If so, is it correct?
        #  - Is the user guessing a single letter?
        #     - If so, you'll need your check() function.
        #  - Is the user's guess invalid (the wrong length)?
        #
        #Also, don't forget to keep track of the valid guesses.

    print('{} is it! It took {} tries.'.format(word, len(guesses)))
    
main()