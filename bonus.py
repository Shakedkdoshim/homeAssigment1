
def a():
    age=25
    height=5.8
    name="Alex"
    print(type(age))
    print(type(height))
    print(type(name))

def b():
    num1 = int(input("Enter numer: "))
    num2 = int(input("Enter more numer: "))
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)

def c():
    x=10
    x+=5
    print(x)

def d():
    num1 = int(input("Enter numer: "))
    num2 = int(input("Enter more numer: "))

    if num1 > num2:
        print(num1, "is greater than" ,num2)
    elif num2 > num1:
        print(num2, "is greater than" ,num1)
    else:
        print(num1, "equal to" ,num2)

def e():
    a=5
    b=7
    if a != b:
        print("a and b are not equal.")
    else:
        print("a and b are equal.")

def f():
    number = int(input("Enter numer: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def g():
    base=9
    result = base ** 3
    print(result)

def h():
    a = int(input("Enter numer: "))
    b = int(input("Enter more numer: "))
    c = input("Enter opertor: ")

    if c=='+':
        print(a+b)
    elif c=='-':
        print(a-b)
    elif c == '*':
        print(a*b)
    elif c == '/':
        print(a/b)
    else:
        print("unexpected operator")

def I():
    num1 = int(input("Enter numer: "))
    if num1 > 0:
        print("number is positive")
    elif num1 < 0:
        print("number is negative")
    else:
        print("number is zero")

def j():
        numbers = [10, 20, 30, 40, 50]
        print("First element:", numbers[0])
        print("Last element:", numbers[4])
def l():
    user = input("Please Enter your name:")
    print(f"Your name is {{user}} and you are a devops engineer")


