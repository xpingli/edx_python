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
        


