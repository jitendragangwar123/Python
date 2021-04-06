def all_total(*args):
    total=0
    for num in args:
        total+=num
    return total

print(all_total(1,2,3))   


def to_power(num,*args):
    if args:
        print(i*num for i in args)
    else:
        return "u did not pass args"

print(to_power(3,2,3,4))   

def multiply_num(num,*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply

print(multiply_num(2,3,4))





def func(l,**kwargs):
    if kwargs.get("reverse_str")==True:
        return [name[: :-1].title() for name in l]
    else:
        return [name.title() for name in l]

l=["harshit","mohit"]
print(func(l,reverse_str = True))    






