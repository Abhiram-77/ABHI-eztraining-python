#dt=02-02-23
#crt_day-4_content

#dictionary comprehension

dic = {n:n*n for n in range(1,5)}
print("the created dictionary is:",dic)
print()

#creating a dictionary using another dictionary
#calculating product price for 5 units

old_dic = {'rice':60,'dhaal':40,'oil':60}
new_dic = {products:price*5 for (products,price) in old_dic.items()}
print(new_dic)
print()

#creating a dictionary using another dictionary
#with conditions

old_dic = {'vamsi':21,'sai':23,'karthik':18}
new_dic = {name:age+5 for (name,age) in old_dic.items() if age>20}
new_dic['krish'] = 23
print(new_dic)
print()

#creating a dictionary using a list and assigning the values randomly to list items

import random
li = ['vamsi','sai','lasya','ram','teja','surya']
dic = {}
for i in li:
    dic[i] = random.randint(10,101)
print(dic)
print()

#using dictionary comprehension
import random
li = ['vamsi','sai','lasya','ram','teja','surya']
dic = {names:random.randint(10,101) for names in li}
print(dic)
print()

#creating a dictionary using two lists and dictionary comprension

l = ['a','b','c','d']
li = [1,2,3,4]
dic = {a:b for (a,b) in zip(l,li)}
print(dic)
print()

l1 = ['vamsi','sai','lasya','teja','surya']
l2 = {names:random.randint(250,400) for names in l1}
dic = {a:(b/400)*100 for (a,b) in l2.items()}
print(dic)
print()


#intrduction to strings

s = "hi i'am vamsi"
print(s)
print()

#s = "hi i'am "vamsi"" # it causes error
#print(s)
print()

s = "hi i'am \"vamsi\""
print(s)
print()

#string operations

s = "Vamsi"
print("the upper case of string s is:",s.upper())
print()
print("the lower case of string s is:",s.lower())
print()
print(s.capitalize())
print()
print("replace the last letter of string s:",s.replace('i','hy'))
print()
print(s.strip())
print()
print("splitting the string s at letter 'm' is:",s.split('m'))
print()
print(s.center(3,'*'))
print()
print("the count of 'a' in string s is:",s.count('a'))
print()
print("the count of 'v' in string s after index 3:",s.count('v',3,len(s)))
print()
print(s.endswith('a',0,len(s)))
print()
print("the index of 'm' in string s is:",s.find('m',0,len(s)))   #generates -1 if letter does not exit in start and end index
print()
print(s.index('s'))
print()
print("the index of 's' in string s after index 2 is:",s.index('a',0,len(s)))  #generated error if letter dose not exit in start and end index
print()
print(s.istitle())
print()
s = "hii'amvamsi"
print(s.islower())
print()
print(s.isupper())
print()
print(s.istitle())
print()
print("the max character in string s is:",max(s))
print()
print("the min character in string s is:",min(s))
print()
print(s.startswith('hi',0,len(s)))
print()

#mutable vs immutable

#mutable - can be changed after creation ex:list,set,dictionary
#immutble - can not be changed after creation ex: int,float,string,bool,tuple

#immutable

#integer
a = 235
print("addresss of a:",id(a))
print()
a = 422
print("addresss of a after reassigning to a:",id(a))
print()


#float

f = 34.332
print("addresss of f:",id(f))
print()
f = 23.42
print("addresss of f after reassigning to f:",id(f))
print()

#string

s = "vamsi"
print("addresss of a:",id(s))
print()
s = "vamshy"
print("addresss of s after reassigning to s:",id(s))
print()


#mutable

#list
li = [235,'sfg',38.324]
print("addresss of list li:",id(li))
print()
li.append(53)
print("addresss of list li after appending a value:",id(li))
print()

#set
st = {45,23,6,2,63}
print("addresss of set st :",id(st))
print(st.add(93))
print("addresss of set st after appending a value:",id(st))
print()


#math module
import math
print("ceil of 21.32:", math.ceil(21.32))
print()
print("floor of 38.82:", math.floor(38.82))
print()
print("sqrt of 43:", math.sqrt(23))
print()
print("factorial of 4:", math.factorial(4))
print()
print("power of 3,5:", math.pow(3,5))
print()
print("remanider of 81,4:", math.fmod(81,4))
print()
