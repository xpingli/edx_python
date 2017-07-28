def loadWords(txt):
    """
    txt: a string, 'words.txt';
    
    returns a list containing all the words.
    """
    
    filename = txt
    
    print('Loading words from', filename)
    fh = open(filename, 'r')
    
    
    words = []
    for word in fh:
        word = word.strip().lower()
        words.append(word)
        
    print('     {} words loaded'.format(len(words)))
    print('PlayGame not yet implemented')
            

    return words
            
