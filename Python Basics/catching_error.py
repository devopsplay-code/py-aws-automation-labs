try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero ❌")
except ValueError:
    print("Please enter a valid number ❌")
