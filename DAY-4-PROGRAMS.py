#dt=02-02-23
#crt_day-4_programs

#question-1

#find wheather a particular character is present or not

s = input("enter a string:")
c = input("enter a character to find its present in given string:")
for i in s:
    if i==c:
        print("the given character is present in given string")
        break
else:
    print("the given character is not present in given string")
print()


#question-2

#palindrom of string containing the number

s = input("enter a string containing a digit:")
t = s[::-1]
if s==t:
    print("the given string is palindrom")
else:
    print("the given string is not a palindrom")

print()


#question-3

#find space in given string and no of spaces in string

s = input("enter a string with spaces:")
c=0
for i in s:
    if i==' ':
        c+=1
if c==0:
    print("their is no spaces in given string")
else:
    print("the no of spaces are:",c)
print()


#question-4

#find the no of vowels in the given string

li = ['a','e','i','o','u','A','E','I','O','U']
s = input("enter the string:")
c=0
for i in s:
    if i in li:
        c+=1
print(c)

