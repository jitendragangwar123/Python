func=lambda s:len(s)>5
print(func('abcd'))



fun=lambda a,b:a*b 
print(fun(2,3))




fun = lambda a,b:a+b 
print(fun(1,4))


fun = lambda a,c:a**c
print(fun(2,3))

fun = lambda a,c:a**c 
print(fun(2,4))

fun = lambda a,c:a**c 
print(fun(2,7))





fun = lambda a,c:a+c 
print(fun(5,6))





fun = lambda a,d:a**d 
print(fun(3,4))


def find_pos(names,target):
    for pos,name in enumerate(names):
       if name==target:
            return pos
    return -1
names=["abc","bdjh","yyeuj"]
print(find_pos(names,"jdjdk"))







