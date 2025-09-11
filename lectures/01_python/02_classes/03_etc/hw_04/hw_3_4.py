import calculator

def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
        result = calculator.add(a, b)
    elif operator == '-':
        result = calculator.subtract(a, b)
    elif operator == '*':
        result = calculator.multiply(a, b)
    elif operator == '/':
        result = calculator.divide(a, b)
    else:
        result = "Invalid operator"

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()