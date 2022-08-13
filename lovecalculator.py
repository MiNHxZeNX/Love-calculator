print("Welcome to Love Calculator !")
name1 = input("What is your name? ")
name2 = input("What is your partner name? ")
stRing = name1 + name2
lowCase = stRing.lower()
t = lowCase.count("t")
r = lowCase.count("r")
u = lowCase.count("u")
e = lowCase.count("e")
true = t+r+u+e
l = lowCase.count("l")
o = lowCase.count("o")
v = lowCase.count("v")
e = lowCase.count("e")
love = l+o+v+e

loveSc = str(true)+str(love)
loveScore = int(loveSc)
if (loveScore<=10) or (loveScore>=90):
    print("Your love score is "+ loveSc + " ,You go together like coke and mentos")
elif (loveScore>=40 and loveScore<=50):
    print("Your love score is "+ loveSc + " ,You are alright together.")
else:
    print("Your love score is "+ loveSc)
