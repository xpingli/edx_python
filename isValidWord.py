    
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
