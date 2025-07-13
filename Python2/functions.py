def greet(name):
    print(f"Hello, {name}")

greet("Alice")

def add(a, b):
    return a + b

result = add(2, 3)
print(result)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Cassey", "Good morning")