user_info="harshit 24".split()
print(user_info)


user="harshit 24".split(",")
print(user)

name,age="harshit, 24".split(",")
print(name)
print(age)


name=["harshit","24"]
print(",".join(name))





n=int(input("enter the num: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()



