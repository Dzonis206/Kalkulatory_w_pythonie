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