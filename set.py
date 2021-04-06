s={1,2,3,4,3,4,3,5}
print(s)


print(list(s))

s.add(4)
print(s)
s.remove(2)
s.discard(10)
print(s)
s.clear()
print(s)


square=[i**2 for i in range(1,11)]
print(square) 



names=["jeetu","johney","chotu"]
new_list=[name[0] for name in names]
print(new_list)

new_list1=[name[ : :-1] for name in names]
print(new_list1)
