#WRITE A PROGRAM AFTER CREATING A LIST WITH EVEN NUMBERS WITH IN THE RANGE 1-15 ,NOW APPLY LAMBDA FUNCTION AND CREATEA NEW LIST WHICH SHOULD HAVE THE SQUARE ROOTS OF THE ELEMENTS
import math
L=[]
for i in range(1,15):
    if (i%2==0):
       L.append(i)
print(L)
r=map(lambda n:math.sqrt(n),L)
print(list(r))

