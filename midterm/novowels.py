def print_out_novowels(s):
    """
    s: string to convert, containing no vowels.
    if s is a vowel or no vowels already or empty string, it will print out empty string.
    return another s without vowels
    """
    
    try:
        s = str(s)
    except:
        print('S must be a string')
        
    vowels = 'AEIOUaeiou'
    
    new_s = ''
    for i in range(len(s)):
        if s[i] in vowels: new_s += ' '
        else:
            new_s += s[i]
            
            
    return new_s


s = 'I want to swim'
print_out_novowels(s)

def test_printnovowels():
    
    
    # test1
    s = 'I want to swim'
    expected_s = '  w nt t  sw m'
    
    out_s = print_out_novowels(s)
    if out_s == expected_s:
        print('Pass test1')
    else:
        print('Failed test1')
            
    # test2
    s = 'a'
    expected_s = ' '
    
    out_s = print_out_novowels(s)
    if out_s == expected_s:
        print('Pass test2')
    else:
        print('Failed test2')

    # test 3
    s = ''
    expected_s = ''
    
    out_s = print_out_novowels(s)
    if out_s == expected_s:
        print('Pass test3')
    else:
        print('Failed test3')
        
        
    # test 4
    s = '0'
    expected_s = '0'
    
    out_s = print_out_novowels(s)
    if out_s == expected_s:
        print('Pass test4')
    else:
        print('Failed test4')
        
        
test_printnovowels()
