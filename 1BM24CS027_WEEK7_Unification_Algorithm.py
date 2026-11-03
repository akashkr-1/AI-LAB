
# General Unification Algorithm in First Order Logic

def is_variable(x):
    return isinstance(x, str) and x.startswith('?')


# Apply substitutions
def substitute(expr, subst):
    if is_variable(expr):
        while expr in subst:
            expr = subst[expr]
        return expr

    if isinstance(expr, tuple):
        return tuple(substitute(x, subst) for x in expr)

    return expr


# Occurs check
def occurs(var, expr, subst):
    expr = substitute(expr, subst)

    if var == expr:
        return True

    if isinstance(expr, tuple):
        return any(occurs(var, x, subst) for x in expr)

    return False


# Unification function
def unify(x, y, subst=None):

    if subst is None:
        subst = {}

    x = substitute(x, subst)
    y = substitute(y, subst)

    # Step 1: Identical expressions
    if x == y:
        return subst

    # Step 2: First expression is a variable
    if is_variable(x):
        if occurs(x, y, subst):
            return None

        subst[x] = y
        return subst

    # Step 3: Second expression is a variable
    if is_variable(y):
        if occurs(y, x, subst):
            return None

        subst[y] = x
        return subst

    # Step 4: Both expressions must be compound terms
    if isinstance(x, tuple) and isinstance(y, tuple):

        # Check predicate symbols
        if x[0] != y[0]:
            return None

        # Check number of arguments
        if len(x) != len(y):
            return None

        # Unify corresponding arguments
        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    # Step 5: Unification failure
    return None


# Convert user input into logical expression
def parse_expression(s):
    s = s.strip()

    # If expression has no arguments
    if '(' not in s:
        return s

    name, args = s.split('(', 1)
    args = args[:-1]

    # Split arguments
    result = []
    depth = 0
    start = 0

    for i, ch in enumerate(args):
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        elif ch == ',' and depth == 0:
            result.append(args[start:i].strip())
            start = i + 1

    result.append(args[start:].strip())

    return (name.strip(),) + tuple(
        parse_expression(arg) for arg in result
    )


# Main program
print("UNIFICATION IN FIRST ORDER LOGIC")

expr1 = input("Enter first expression: ")
expr2 = input("Enter second expression: ")

x = parse_expression(expr1)
y = parse_expression(expr2)

result = unify(x, y)

if result is None:
    print("\nUnification FAILED")

else:
    print("\nUnification SUCCESSFUL")

    print("Substitution:")
    if result:
        for var, value in result.items():
            print(var, "=", value)
    else:
        print("No substitution required")

    print("\nUnified Expression 1:")
    print(substitute(x, result))

    print("Unified Expression 2:")
    print(substitute(y, result))
