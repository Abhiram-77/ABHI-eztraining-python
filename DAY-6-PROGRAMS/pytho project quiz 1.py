q1="""who is the successfull caption of indian cricket team?
A.kapil Dev
B.Mahendra Singh Dhoni
C.Virat Kohli
D.Rohit Sharma"""
q2="""who is best wrestler of all time?
A.Great khali
B.UNder Taker
C.Roman Reigns
D.John Cena"""
q3="""What is the most friendly dog breed?
A.Labrador
B:pug
C.Golden Retreiver
D.Rottweiler"""
q4:"""who is the costliest player in ipl auction history?
A.Ishan kishan
B.Ben stokes
C.Deepak Chahar
D.Sam Curran"""
q5:"""Which company developed world's first Touch Screen Mobile phone?
A.Motorola
B.IBM
C.Apple
D.Samsung"""
questions={q1:"B",q2:"D",q3:"C",q4:"D",q5:"B"}
name=input("Hi what's your name?")
print("hello",name,"welcome to the Quiz.")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip the question?(Yes/No)")
    if flag1=="Yes":
        continue
    ans=input("enter your answewr:")
    if ans==question(i):
        print("WOW!!You got one point")
        score=score+1
        print("Your current score is:",score)
    else:
        print("Wrong Answer ,You lost one point")
        score=score-1
        print("Your current Score is:",score)
    flag2=input("Do you want to quit?type(Yes/No)")
    if flag2=="yes":
        break
print("your total score is:",score)
