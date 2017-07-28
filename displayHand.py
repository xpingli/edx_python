
def displayHand(hand):
    """
    d: a dictionary containing delt hand;
    returns a string in your hand
    """
    
    display = ''
    for k in hand.keys():
        display = display + ' '.join(list(k * hand[k])) + ' ' # o mm z g j 
        
    return display
