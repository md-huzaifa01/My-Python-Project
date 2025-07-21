def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return None
    return a/b
print("Simple Calculator")
print(""" The operation is defined as
1.Addition 
2.Subtraction
3.Multiplication
4.Divide""")
op=int(input("Enter what you wnat ot do: "))
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
if op==1:
    print("The result is: ", num1,"+",num2, "=", num1+num2)
elif op==2:
        print("The result is: ", num1,"-", num2, "=", num1-num2)
elif op==3:
    print("The result is: ", num1, "*", num2, "=",num1*num2)
elif op==4:
    result=divide(num1,num2)
    if result is not None:
        print("The result is :", num1, "/", num2, result)
    else:
        print("The result is Error because it divide by zero")
else:
    print("Error!, Please check your input and try again.")
