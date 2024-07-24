import random
from fractions import Fraction

def generate_linear_equation():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c

def solve_linear_equation(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' não pode ser zero em uma equação de primeiro grau.")
    return (c - b) / a

def generate_incorrect_option(correct_solution):
    options = [
        correct_solution - 7,
        correct_solution + 7,
        correct_solution * 7
    ]
    incorrect_option = random.choice(options)
    while incorrect_option == correct_solution:
        incorrect_option = random.choice(options)
    return incorrect_option

def format_solution(solution):
    if solution.denominator == 1:
        return f"{solution.numerator}"
    else:
        return f"{solution.numerator}/{solution.denominator}"

def display_equation_and_options(a, b, c, correct_solution, incorrect_solution):
    print(f"Resolva a equação: {a}x + {b} = {c}")
    
    correct_solution = Fraction(correct_solution).limit_denominator()
    incorrect_solution = Fraction(incorrect_solution).limit_denominator()
    
    options = [correct_solution, incorrect_solution]
    random.shuffle(options)
    
    print(f"Opções:")
    for i, option in enumerate(options):
        print(f"{i + 1}. x = {format_solution(option)}")

def main():
    a, b, c = generate_linear_equation()
    correct_solution = solve_linear_equation(a, b, c)
    incorrect_solution = generate_incorrect_option(correct_solution)
    display_equation_and_options(a, b, c, correct_solution, incorrect_solution)

if __name__ == "__main__":
    main()