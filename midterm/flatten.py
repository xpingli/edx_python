def flatten(alist):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    
    [[1,'a',['cat'],2],[[[3]],'dog'],4,5] to [1,'a','cat',2,3,'dog',4,5]
    '''
    new_list = list()
    for x in alist:
        print('new_list: ', new_list)
        if type(x) == list:
            
            new_list = new_list + flatten(x) # if do new_list.append(flatten),you just put your list back, because each
            # iteration will set new_list to blank. This way, new_list can store previous flattened element 
        else:
            new_list.append(x)
            
    return new_list
        



alist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(alist))
