num=[1,2,4,5,12,4,4]
print(min(num))
print(max(num))


def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(num))



def f_list(l):
    count=0
    for i in l:
        if type(i)==list:
           count+=1
    return count 


mix=[1,1,4,[1,4,23,4],[121,1,12,12,3]]

print(f_list(mix))

