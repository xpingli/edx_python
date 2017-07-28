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
        