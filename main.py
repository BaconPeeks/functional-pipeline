import math
import os

def main():
    """
    CLI orchestration function.
    Prompts the user for input and calls the appropriate functions to solve the problem.
    """
    print("1) Solve quadratic (where a = 1)\n2) multiply exponets\n3)Divide Exponets")
    choice = input("Choose an option: ")
     
    if not choice.isdigit(): 
        raise ValueError("Please input a number.")
    
    if choice == "1":
        clear_screen()
        b = int(input("Enter coefficient b:\n "))
        c = int(input("Enter coefficient c:\n "))
        answer = solve_quadratic(b, c)
        print(f"The roots are: {answer}")
    elif choice == "2":
        clear_screen()
        a = int(input("First exponet:\n"))
        b = int(input("Second exponet:\n"))
        result = multiply_exponents(a,b)
        clear_screen()
        print(f"REsulting exponet: {result}")
    elif choice == "2":
        clear_screen()
        a = int(input("First exponet:\n"))
        b = int(input("Second exponet:\n"))
        result = subtract_exponets(a,b)
        clear_screen()
        print(f"Sum of exponets: {result}")

        


def solve_quadratic(b, c):
    """
    Solves the quadratic equation of the form x^2 + bx + c = 0 by finding two numbers that multiply to c and add to b.
    

    :return: a factored form if possible, 
    otherwise returns a message indicating that it is not factorable over the integers.
    """
    pair = find_ac_pair(b, c)
    if pair is None:
        return "Not factorable over the integers."
    m, n = pair 
    return f"(x+{m})(x+{n})"


def subtract_exponets(a,b):
    """
    Subtracts two exponets using x^a / x^b = x^(a-b)
    """
    return a - b

def multiply_exponents(a, b):
    """
    Adds two exponents using the law:
    x^a * x^b = x^(a+b)
    """
    return a + b

def find_ac_pair(b, c):
    """
    Finds integers m and n such that:
    m * n = c
    m+ n = b

    :param b: the first coefficient of the quadratic equation
    :param c: the second coefficient of the quadratic equation
    """
    for i in range(-abs(c), abs(c) + 1):
        if i == 0:
            continue
        if c % i == 0:
            j = c // i
            if i + j == b:
                return i, j
    return None

        
def clear_screen():
    """
    Helper function to clear the terminal screen. Works on both Windows and Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    main()