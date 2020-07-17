"""function to display group of strings"""

txt = input("Enter a string:")
txt1 = txt.split()


def group_strings(t):
    util_func = lambda x, y: x[0] == y[0]
    res = []
    for sub in t:
        ele = next((x for x in res if util_func(sub, x[0])), [])
        if ele == []:
            res.append(ele)
        ele.append(sub)

        # print result
    return res

'''


def group_strings(t):
    ele = []
    for i in t:
        for j in range(1,len(t)):
            
            
'''
print(group_strings(txt1))
