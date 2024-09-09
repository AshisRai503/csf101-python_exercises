x = 10  # Global variable

def print_x():
    x = 20  # Local variable
    print(f"Local x: {x}")

print_x()
print(f"Global x: {x}")

count = 0

def increment():
    global count
    count += 1
    print(f"Count: {count}")

increment()
increment()
print(f"Final count: {count}")

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner x: {x}")

    inner()
    print(f"Outer x: {x}")

outer()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
