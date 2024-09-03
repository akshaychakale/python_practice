num1 = int(input('Enter 1st number:'))
num2 = int(input('Enter 2nd number:'))


def swap_number(num1, num2):
    print("before swapping num1={0} & num2= {0}".format(num1, num2))
    a = num1
    b = num2

    a = a + b
    b = a - b
    a = a - b

    print("after swapping num1={0} & num2= {0}".format(a, b))

swap_number(num1, num2)
