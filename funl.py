num=[1,3,4,6,57,78,9,0,4,]
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num)) 



def square_list(l):
    sqr=[]
    for i in l:
       x= i**2
       sqr.append(x)

    return sqr
num=list(range(1,11))    
print(square_list(num))

