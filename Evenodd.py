num = input("Enter a Number to check Even or Odd: ")
num = int(num)
if(num%2==0):

    print("Enterd Number ",num,"is Even.")
else:
    print("Enterd Number ",num,"is Odd.") 
#using function

def EvenOdd(num1):
    if num1%2==0:
        print("This is a Even Number")
    else:
        print("This is an Odd Number")
EvenOdd(num)