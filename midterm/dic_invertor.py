def test_dict_invert():
    # test 1
    d = {1:10, 2:20, 3:30}
    expected_d = {10: [1], 20: [2], 30: [3]}
    
    conv_d = dict_invert(d)
    if conv_d != expected_d:
        print('Failed test 1')
    else:
        print('You passed test 1')
    
    # test 2
    d = {1:10, 2:20, 3:30, 4:30}
    expected_d = {10: [1], 20: [2], 30: [3, 4]}
    
    conv_d = dict_invert(d)
    if conv_d != expected_d:
        print('Failed test 2')
    else:
        print('You passed test 2')
        
    # test 3
    d = {4:True, 2:True, 0:True}
    expected_d = {True: [0, 2, 4]}
    
    conv_d = dict_invert(d)
    if conv_d != expected_d:
        print('Failed test 3')
    else:
        print('You passed test 3')
        
        

    
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary
    '''
    
    new_d = {}
    for k, v in d.items():
        new_d[v] = new_d.get(v,[]) + [k]
        new_d[v].sort()
        
    return new_d
        

