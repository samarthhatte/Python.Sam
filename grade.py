score1 = int(input("Enter Your 1st Subject marks: "))
score2 = int(input("Enter Your 2st Subject marks: "))
score3 = int(input("Enter Your 3st Subject marks: "))
score4 = int(input("Enter Your 4st Subject marks: "))
score5 = int(input("Enter Your 5st Subject marks: "))

score = (score1+score2+score3+score4+score5)/500*100
print(score)

if   90 <= score:
    print("Grade: A")
elif 80 <=score:
    print("Grade: B")
elif 70 <=score:
    print("Grade: C")
elif 60 <= score:
    print("Grade: D")
else: 
    print("Grade: F")
