try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a / b
    print('a = ', a)
    print('b = ', b)
    print('a / b = ', c)
except ZeroDivisionError:
    print("You cannot divide a number by zero.")
except ValueError:
    print("Please provide integer values only.")
finally:
    print("ha ha ha")