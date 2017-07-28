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
        
def isValidWord(word, hand, wordlist):
    """
    word: a string, the word you come up with from the hand
    hand: a dictionary, containing the letters you have got
    wordlist: a list, the provided wordlist
    
    returns: a boolean, True if the word is valid in the word list
                        False if the word is not in the word list.
    """
    
    hand_copy = hand.copy()
    word_copy = wordlist.copy()  
    word_set = set(word_copy)
    
    your_word = getFreqDict(word)
    

    if word not in word_set:
            
        return False
        
    else:
        
        for k in your_word.keys():
                        
            if (k not in hand_copy.keys()) or (your_word[k] > hand_copy[k]):
                
                return False
        
            else:
                return True
            
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
        
        isvalid = isValidWord(word, hand, wordlist)
    
        if isvalid == True:
            
            total_score += GetScore(word, n)
            print(' "{}" earned {} points. Total Score: {}'.format(word, GetScore(word, n), total_score))
            
            hand = updateHand(hand, word)
            
        else:
            print('Invalid Word: Please try again')
            
        value = calculateHandlen(hand)
            
            
    return '\nRun out of letters. Total Score: {} points'.format(total_score)






def playGame(wordlist):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    while True:
        
        try:
            instruction = input("""Enter [n] to play a new hand\n[r] to replay the last hand\n[e] to exit the game: """)
        
            if instruction == 'n':
            
                hand = dealHand()
            
                playHand(hand, wordlist)
            
            elif instruction == 'r':
            
                try:
                    playHand(hand, wordlist)
                
                
                except:
                    print('You have not played a new hand yet. Please try a new hand first')
                    return playGame(wordlist)
            
            elif instruction == 'e':
                    break
                    
            else:
                print('Invalid Command')
                return playGame(wordlist)
        
        except:
        
            print('Invalid input')
            return playGame(wordlist)
        


if __name__ == '__main__':
    wordlist = loadWords()     
    playGame(wordlist)        
    