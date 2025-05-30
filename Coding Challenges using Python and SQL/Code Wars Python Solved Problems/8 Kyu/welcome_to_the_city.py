# Question: Welcome to the City
# Categories: 8 Kyu

def say_hello(name: str, city: str, state: str) -> str:
    full_name = ' '.join(name)
    return f'Hello, {full_name}! Welcome to {city}, {state}!'