user={'name':'harshit','age':28,'sex':'male'}
print(user)
print(user['name'])


user1={}
user1['name']='mohit'
user1['age']=26
print(user1)



if 'mohit' in user1.values():
     print("yes")
     

for i in user:
     print(i)

for i in user.values():
     print(i)


user_item=user.items()
print(user_item)



for key,value in user.items():
     print(f"key in {key} and value is {value}")


popped_item=user.popitem()
print(user) 
print(popped_item)    


users={'name':'mohit','age':21,'sex':'male' }
users1={'name':'rohit','age':23}
users.update(users1)
print(users)

def cube_finder(n):
     cubes={}
     for i in range(1,n+1):
          cubes[i]=i**3
     return cubes 
print(cube_finder(10))   

def word_counter(s):
     count={}
     for char in s:
          count[char]=s.count(char)
     return count
print(word_counter('harshit')) 


d={}
name=input("what is your name: ")
age=int(input("what is your age: "))
fav_movie=input(("what is your fav_movie: "))
d['name']=name
d['age']=age
d['fav_movie']=fav_movie
for key,value in d.items():
      print(f"{key}:{value}")


