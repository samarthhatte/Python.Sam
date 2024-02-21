def caculater(num1, num2, operater):
    if operater == '+':
        return num1+num2
    elif operater == '-':
        return num1 - num2
    elif operater =='/':
        return num1 / num2
    elif operater =='*':
         return num2 * num1
    else:
        return "Invalid operator"
    
    result = caculater (5,3,'*')
    print(result)
    

    

