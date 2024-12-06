def addNumbers(x,y):
    return x + y

def multiplyNum(x,y):
    return x * y

def divideNum(x,y):
    return x / y

def subtractNum(x,y):
    return x - y

#print("Hello Calculator \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")
choice = int(input("Hello Calculator \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \nChoose an operation: "))
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter second Number: "))

match choice:
    case "1":
        print(addNumbers(num1, num2))
    case 2:
        print(subtractNum(num1, num2))
    case 3:
        print(multiplyNum(num1, num2))
    case 4:
        print(divideNum(num1, num2))

print("Yeey")