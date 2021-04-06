def reverse_list(l):
    l.reverse()
    return l    
    

num=list(range(1,10))
print(reverse_list(num))


def rev_list(l):
    return l[ : :-1]

print(rev_list(num)) 



def res_list(l):
    reverse=[]
    for i in range(len(l)):
        x=l.pop()
        reverse.append(x)
    return reverse
n=[1,3,2,4,5,6]    
print(res_list(n))    




def revs_list(l):
    ele=[]
    for i in l:
       ele.append(i[ : :-1])

    return ele
num=["abc","bnd","hgfn"]  
print(revs_list(num))  



def odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output 

num=[1,2,4,3,7,9,4,8,0]
print(odd_even(num))
                
    
def common_list(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output 

print(common_list([1,2,3,4,1,4],[1,3,2,5,6]))


















