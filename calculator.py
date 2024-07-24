num1 = float(input("please enter your first number: "))
p = input()
num2 = float(input("please enter your second number: "))


def A(x, y):
    return x + y
def S(x, y):
    return x - y
def M(x, y):
    return x * y
def D(x, y):
    return x / y

if p ==  "+":
    print(A(num1,num2))
elif p ==  "-":
    print(S(num1,num2))
elif p ==  "*":
    print(M(num1,num2))
elif p ==  "/":
    print(D(num1,num2))
