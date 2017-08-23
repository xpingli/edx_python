import string

def load_words(filename):
    """
    filename: a string, the file containing the words to load
    
    returns a list of words, words in lowercase
    """
    with open(filename, 'r') as words:
        
        lineofword = words.readline() # use readline to save memory
        word_list = lineofword.split()
        print(' ', len(word_list), 'loaded')
        
        return word_list


def is_word(word_list, word):
    """
    determine if the word is the valid word, ignoring
    capitalization and punctuation
    
    word_list: list of words in the dictionary
    
    word: a string of word
    
    Returns a boolean
    """
    
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    
    return word in word_list


def get_story(filename):
    """
    filename: a string, the file name for the story but encrypted
    """
    with open(filename, 'r') as fh:
        
        story = str(fh.read())
        
        return story
        
        
WORDLIST_FILENAME = 'words.txt'
## Message class    

class Message(object):
    
    def __init__(self, text):
        self.text = text
        self.valid_word = load_words(WORDLIST_FILENAME)
           
    def __str__(self):
        return str(self.text)
    
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.text
        
        
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_word[:]
    
    def build_cipher_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        assert type(shift) == int, 'shift must be an integer'

        if shift < 0 or shift >= 26:
            raise ValueError("0 <= shift < 26")
        
        letter_56_list = list(string.ascii_uppercase + string.ascii_lowercase)
    
    

        letter_56_dict = {}
        for i in range(len(letter_56_list)):
            if i < 26:
                if i+shift <= 25:
                    letter_56_dict[letter_56_list[i]] = letter_56_list[i + shift]
                elif i+shift > 25:
                    letter_56_dict[letter_56_list[i]] = letter_56_list[i + shift - 26]
            elif i >= 26:
                if i+shift <= 51:
                    letter_56_dict[letter_56_list[i]] = letter_56_list[i + shift]
                elif i+shift > 51:
                    letter_56_dict[letter_56_list[i]] = letter_56_list[i + shift - 26]
                
        return letter_56_dict
    
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
                 down the alphabet by the input shift
        '''

        assert type(shift) == int, 'shift must be an integer'

        if shift < 0 or shift >= 26:
            raise ValueError("0 <= shift < 26")
        
    
        texts = self.text
        letter_dict = self.build_cipher_dict(shift)
        
        new_msg = ''
        for i in texts:
            if i in letter_dict.keys():
                new_msg = new_msg + letter_dict[i]
            else:
                new_msg = new_msg + i
                
        return new_msg
    
class PlaintextMsg(Message):
    
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_cipher_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
    
    def get_encrypt_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()
    
    def get_message_text_encrypted(self):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert type(shift) == int, 'shift must be an integer'

        if shift < 0 or shift >= 26:
            raise ValueError("0 <= shift < 26")
            
        PlaintextMsg.__init__(self,self.text, shift)
        
        
class ciphertextMsg(Message):
    
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        valid_wd = self.valid_words

        
        
        result = []
        for shift in range(1, 26):
            
            bestscore = 0
            decipher = Message.apply_shift(self, 26 - shift) # string type has no apply_shift
            strip_text = decipher.split()
            
            for word in strip_text:
                if is_word(valid_wd, word):
                    bestscore += 1 
            
            result.append((bestscore, 26-shift, decipher))

        all_shift = sorted(result, reverse = True) 
        
        best = all_shift[0][0]
        
        top = [(i[1], i[2]) for i in all_shift if i[0] == best]
        

        return top
            
##Example test case (PlaintextMessage)
#plaintext = PlaintextMsg('hello', 2)
#print('Expected Output: jgnnq')
#print('Actual Output:', plaintext.get_message_text_encrypted())
#    
##Example test case (CiphertextMessage)
#ciphertext = ciphertextMsg('jgnnq')
#print('Expected Output:', (24, 'hello'))
#print('Actual Output:', ciphertext.decrypt_message())


filename = 'story.txt'


def decrypt_story(filename):
    """
    filename: a string, containing the encrypted story
    
    return: decrptyed story
    """
    
    string = get_story(filename)
    
    decipher_text = ciphertextMsg(string)
    
    story = decipher_text.decrypt_message()

    return story


