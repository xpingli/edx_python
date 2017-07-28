def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here

    d_intersect = {i: f(d1[i], d2[i]) for i in d1.keys() if i in d2.keys()}

    d_diff = {}
    for i in d1.keys():
        if not i in d2.keys():
            d_diff[i] = d1[i]
            
    for j in d2.keys():
        if not j in d1.keys():
            d_diff[j] = d2[j]


    return (d_intersect, d_diff)


