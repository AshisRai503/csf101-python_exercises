number = 10
if number > 0:
    print('The number is Positive')
else:
    print('The number is Negative')

number = 0
if number > 0:
    print('The number is Positive')
elif number < 0:
    print('The number is Negative')
else:
    print('The number is Zero')

score = 85
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
print(f'Your grade : {score}')

number = 7
result = "Even" if number % 2 == 0 else "odd"
print(f'The number is {result}')

num1 = 10
num2 = 5
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")
    
    
    