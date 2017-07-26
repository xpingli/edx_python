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
 
    
print(GetScore('waybill', 7))
        