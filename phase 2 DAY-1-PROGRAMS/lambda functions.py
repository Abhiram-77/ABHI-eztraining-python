#anonymous function
L=[1,2,3]
r=map(lambda x:x+x,L)
print(list(r))

res=map(lambda n:pow(n,2),L)
print(list(res))

name="sam"
(lambda name:print(name))(name)
