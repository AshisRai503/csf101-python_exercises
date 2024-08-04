def greet():
    print("Hello, World!")

greet()

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def square(number):
    return number ** 2

result = square(5)
print(result)

def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))