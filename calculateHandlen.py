def calculateHandlen(hand):
    """
    Returns the length (number of letters) in current hand
    
    hand: a dictionary (string:int)
    returns a integer
    """
    length = sum(hand.values())
    
    return length
    