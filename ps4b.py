import random
import string

def loadWords():
    """
    txt: a string, 'words.txt';
    
    returns a list containing all the words.
    """
    
    filename = 'words.txt'
    
    print('Loading words from', filename)
    fh = open(filename, 'r')
    
    
    words = []
    for word in fh:
        word = word.strip().lower()
        words.append(word)
        
    print('     {} words loaded'.format(len(words)))
    print('PlayGame not yet implemented')
            

    return words


def getFreqDict(string):
    """
    string: a string of letters as input.
    
    returns a dictionary with the frequency of each letter.
    """
    
    d = {}
    for i in string:
        i = i.lower()
        d[i] = d.get(i, 0) + 1
        
    return d




def dealHand():
    """
    returns n lowercase letters
    """
    import random
    import string
    
    vowels = 'aeiou'
    constant = 'bcdfghjklmnpqrstvwxyz'
    
    maxint = max(list(map(len, wordlist)))
    
    n = random.randint(5, maxint) 
    
    # 1/3 vowls
    n_vowl = n // 3
    n_constant = n - n//3
    
    get_vowl = random.choices(vowels, k = n_vowl)
    get_constant = random.choices(constant, k = n_constant)
    
    strings = ''.join(get_vowl + get_constant)
    
    hand = getFreqDict(strings)
    
    return hand


#=====================================================================================================
def displayHand(hand):
    """
    d: a dictionary containing delt hand;
    returns a string in your hand
    """
    
    display = ''
    for k in hand.keys():
        display = display + ' '.join(list(k * hand[k])) + ' ' # o mm z g j 
        
    return display


def updateHand(hand, word):
    """
    hand: a dictionary, the letters in your hand
    word: the word you used, assume it is valid
    returns updated dictionary containing the frequency of the remaining letters
    """
    #new_hand = dict()
    
    hand_copy = hand.copy()
    
    for i in word:
        
        if i in hand.keys():
            
            hand_copy[i] = hand_copy.get(i, 0) - 1 # get(i, default) if i in the key, return the d[i] value
            # if i is not in the key, then return 0
            
    return hand_copy
#=================================================================================================
#==============================================================================================       
def isValidWord(word, hand, wordlist):
    """
    word: a string, the word you come up with from the hand
    hand: a dictionary, containing the letters you have got
    wordlist: a list, the provided wordlist ( can be a tuple)
    
    returns: a boolean, True if the word is valid in the word list
                        False if the word is not in the word list.
    """
    
    hand_copy = hand.copy()
    word_copy = wordlist.copy()
    
    if type(word_copy) == tuple:
        print('wordcopy:',word_copy)
        word_extract = [item[1] for item in word_copy]
        word_set = word_extract
    elif type(word_copy) == list:
        word_set = word_copy
    elif type(word_copy) == set:
        word_set = word_copy
        
    your_word = getFreqDict(word)
    
    if word not in word_set:
   
        return False
        

        
    for k in your_word.keys():
        if not k in hand_copy.keys(): 
            return False
        elif your_word[k] > hand_copy[k]:
            return False
        
    return True


#=================================================================================
def GetScore(word, n):
    """
    word: a word strings, assume it is a valid word
    
    score is calcualated according to the score dictionary
    such that add up the sum of each letter in the word, then multiplied by length of the 
    word.
    
    special condition is first hand dealing and used up all the letters: bonus point 50
    
    return a scores
    """
    
   # Scoring
   # The score for the hand is the sum of the scores for each word formed.
   # The score for a word is the sum of the points for letters in the word, 
   # multiplied by the length of the word, plus 50 points if all n letters are 
   #        used on the first word created.
   # Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, 
   #        D is worth 2, E is worth 1, and so on.
   # We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase 
   #        letter to its Scrabble letter value.
   # For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, 
   #       then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check 
   #       that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
   # As another example, if n=7 and you make the word 'waybill' on the first try,
   #      it would be worth 155 points (the base score for 'waybill' is 
   #      (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).
                                

    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    # calculate score for each letter:
    score = 0
    for i in word:
        
        score = score + SCRABBLE_LETTER_VALUES[i]
        
    if len(word) < n:
            
        score = score*len(word)
        
    elif len(word) == n:
            
        score = score*len(word) + 50
        
    return score
 
    
def calculateHandlen(hand):
    """
    Returns the length (number of letters) in current hand
    
    hand: a dictionary (string:int)
    returns a integer
    """
    length = sum(hand.values())
    
    return length      
            


def playHand(hand, wordlist):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    def calculateHandlen(hand):
        """
        Returns the length (number of letters) in current hand
    
        hand: a dictionary (string:int)
        returns a integer
        """
        length = sum(hand.values())
    
        return length
    
    n = calculateHandlen(hand)
    value = calculateHandlen(hand)
    total_score = 0
    
    while value > 0:

        
        print('\nCurrent Hand: {}'.format(displayHand(hand)))
        
        word = input('Enter a word, or "." to indicate that you are finished: ').lower()
    
        if word == '.':
            print('Goodby! Total Score: {}'.format(total_score))
            break
        else:
            if isValidWord(word, hand, wordlist):
            
                total_score += GetScore(word, n)
                print(' "{}" earned {} points. Total Score: {}'.format(word, GetScore(word, n), total_score))
                hand = updateHand(hand, word)
                value = calculateHandlen(hand)
            
            else:
                print('Invalid Word: Please try again')
            
        
            
            
    return '\nRun out of letters. Total Score: {} points'.format(total_score)



#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordlist):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    
    # trying to make the program go fast by construct (length, word)
    n = calculateHandlen(hand)
    word_tuplelist = [(len(i), i) for i in wordlist]
    word_tuplelist.sort()
    
    index_word = [i for i, x in enumerate(word_tuplelist) if x[0] <= n]

    if len(index_word) == 0:
        max_idx = 0
        min_idx = 0
    
    max_idx = max(index_word)        
    min_idx = min(index_word)

    
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None

    for item in word_tuplelist[min_idx:max_idx + 1]:
        
        theword = item[1].strip()
        
        if isValidWord(theword, hand, wordlist):
            score = GetScore(theword, n)
            if (score > bestScore):
                bestScore = score
                bestWord = theword

    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordlist):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    n = calculateHandlen(hand)
    value = calculateHandlen(hand)
    # As long as there are still letters left in the hand:
    while (value > 0) :
        # Display the hand
        print("Current Hand: {}".format(displayHand(hand)))
        # computer's word
        word = compChooseWord(hand, wordlist)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordlist)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = GetScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                value = calculateHandlen(hand)
                print()
                
                
        
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#
def playGame2(wordlist):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    
    """
    def askforCom():
        
        inputs = input('Enter [u] for user-play; [c] for computer play: ')
        return inputs
    
    
    while True:
        

        instruction = input("""Enter [n] to play a new hand\n[r] to replay the last hand\n[e] to exit the game: """).lower()
            
                   
        if instruction == 'n':
                
            compYes = askforCom()
                
            if compYes == 'u':
                     
                hand = dealHand()
                playHand(hand, wordlist)
                     
            elif compYes == 'c':
                    
                hand = dealHand()
                compPlayHand(hand, wordlist)

                
            else:
                print('Invalid Command: u for user play, c for computer player')
                return playGame2(wordlist)

            
            
                    
            
        elif instruction == 'r':
            
            compYes = askforCom()
                
            if compYes == 'u':
                    
                try:
                    playHand(hand, wordlist)  
                        
                except:
                    print('You have not played a new hand yet. Please try a new hand first')
                    return playGame2(wordlist)
                    
            elif compYes == 'c':
                        
                try:
                    compPlayHand(hand, wordlist)
                except:
                    print('You have not played a new hand yet. Please try a new hand first')
                    return playGame2(wordlist)
                
            else:
                print('Invalid Command: u for user play, c for computer player')

                return playGame2(wordlist)
            
            
        elif instruction == 'e':
            break
                    
        else:
            print('Invalid Command')
            return playGame2(wordlist)
        

                    
           
        

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordlist = loadWords()
    wordlist = set(wordlist)
    playGame2(wordlist)





