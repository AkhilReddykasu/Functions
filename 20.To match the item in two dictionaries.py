"""To match the item in two dictionaries."""

dict1 = {'1', '2', '3'}
dict2 = {'Python', 'Java', 'Node JS'}


def match_dictionary(d1, d2):
    d3={}
    for i in range(0,len(d1)):
        for j in range(0,i+1):
            d3[d1['i']]=d2['j']

    return d3


print("To match the items in dictionaries", match_dictionary(dict1, dict2))
