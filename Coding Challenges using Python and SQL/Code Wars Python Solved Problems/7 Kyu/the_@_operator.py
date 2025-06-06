# Question: The @ operator
# Categories: 7 Kyu

def evaluate(equation: str) -> int:
    try:
        equation = equation.split(' @ ')

        if len(equation) == 2:
            a = int(equation[0])
            b = int(equation[1])
            return (a + b) + (a - b) + (a * b) + (a // b)
        
        result = (int(equation[0]) + int(equation[1])) + (int(equation[0]) - int(equation[1])) + (int(equation[0]) * int(equation[1])) + (int(equation[0]) // int(equation[1]))
        equation = equation[2:]

        while len(equation) != 0:
            result = (result + int(equation[0])) + (result - int(equation[0])) + (result * int(equation[0])) + (result // int(equation[0]))
            equation = equation[1:]
        
        return result
    
    except ZeroDivisionError:
        return None