import math

def evaluate_expression(expr):
    try:
        return eval(expr)
    except Exception:
        return "Error"

def advanced_operation(expr, op, exponent=None):
    try:
        value = float(expr)
        if op == "x²":
            return str(value ** 2)
        elif op == "√x":
            return str(math.sqrt(value))
        elif op == "1/x":
            return str(1 / value)
        elif op == "xʸ":
            if exponent is not None:
                return str(value ** exponent)
            else:
                return "Error"
        else:
            return "Error"
    except Exception:
        return "Error"
    
import math

def solve_quadratic(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b**2 - 4*a*c
        if a == 0:
            return "Not quadratic"
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"x₁={x1}, x₂={x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"x={x}"
        else:
            return "No real roots"
    except Exception:
        return "Error"