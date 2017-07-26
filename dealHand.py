def dealHand(n):
    """
    returns n lowercase letters
    """
    import random
    import string
    
    letters = string.ascii_lowercase
    
    get_letter = random.choices(letters, k = n)
    
    strings = ''.join(get_letter)
    
    hand = getFreqDict(strings)
    
    return hand