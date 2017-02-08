

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    
    i=0
    s=0
    while i<len(secretWord ):
        if secretWord [i] in lettersGuessed:
            s=s+1
            i=i+1
        else:
            break

    if s==len(secretWord ):
        
        return True
    else:
        return False
        

    




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   
    i=0
    ans=''

    while i<len(secretWord ):
        if secretWord [i] in lettersGuessed:
            ans=ans+secretWord [i]
        
        
        else:
           ans=ans+'_ '
        i=i+1
   
    return ans




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    ans=' '
    import string
    for i in range(0,26):
        if string.ascii_lowercase[i] not in lettersGuessed:
            ans=ans+string.ascii_lowercase[i]  
    return ans


    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    l=len(secretWord)

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+ str(l) + " letters long."

    nog=8
    lettersGuessed1=' '
    i=0
    lettersGuessed=' '
    lettersGuessed1=' '
    while nog!=0:
        print "You have "+str(nog)+" guesses left."
        e=getAvailableLetters(lettersGuessed)
        print "Available letters:"+ str(e)
        
        
        guess=raw_input("Please guess a letter:")
        guessInLowerCase = guess.lower()
        
      
        
        
        v=getAvailableLetters(lettersGuessed)
        print "v="+v
        lettersGuessed=lettersGuessed+guessInLowerCase
       
        if guessInLowerCase in secretWord :
            lettersGuessed1=lettersGuessed1+guessInLowerCase
           
            m=getGuessedWord(secretWord, lettersGuessed)
            u=getAvailableLetters(lettersGuessed)
            w=getAvailableLetters(lettersGuessed1)
            if m==secretWord:
                print"Good guess:",
                print secretWord
       
                break

            elif guessInLowerCase not in v:
                print "Oops! You've already guessed that letter:",
                print m
           
            
           
                        
            else:
                print"Good guess:",
                print m
                print "---------------------------------------------------------------"
       

        
                
        elif guessInLowerCase not in secretWord  :
            if guessInLowerCase not in v:
                 print "Oops! You've already guessed that letter:_"
            else:    
                print "Oops! That letter is not in my word:",
                m=getGuessedWord(secretWord, lettersGuessed)
                print m
                print "-----------------------------------------------------------------"
                nog=nog-1
        
        if nog==0:
            break
        else:
            i=i+1

        

    print "-----------------------------------------------------------------------------"
    q=isWordGuessed(secretWord, lettersGuessed)
    if q==True:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was ."+secretWord  
         
#secretWord = chooseWord(wordlist).lower()
secretWord='cinderella'
k=hangman(secretWord)

