
def tt_entails(KB, alpha, symbols):
    return tt_check_all(KB, alpha, symbols, {})


def tt_check_all(KB, alpha, symbols, model):

    if len(symbols) == 0:
        if pl_true(KB, model):
            return pl_true(alpha, model)
        else:
            return True

    P = symbols[0]
    rest = symbols[1:]

    model_true = model.copy()
    model_true[P] = True

    model_false = model.copy()
    model_false[P] = False

    return (tt_check_all(KB, alpha, rest, model_true)
            and
            tt_check_all(KB, alpha, rest, model_false))


def pl_true(expression, model):
    expression = expression.strip()

    if expression.startswith("not "):
        return not pl_true(expression[4:], model)

    if " or " in expression:
        left, right = expression.split(" or ", 1)
        return pl_true(left, model) or pl_true(right, model)

    if " and " in expression:
        left, right = expression.split(" and ", 1)
        return pl_true(left, model) and pl_true(right, model)

    if expression.startswith("(") and expression.endswith(")"):
        return pl_true(expression[1:-1], model)

    if expression in model:
        return model[expression]

    return bool(model.get(expression, False))


# Main program
symbols = input("Enter proposition symbols: ").split()

KB_input = input("Enter Knowledge Base (KB): ")
alpha_input = input("Enter Query (alpha): ")

KB = lambda model: pl_true(KB_input, model)
alpha = lambda model: pl_true(alpha_input, model)

if tt_entails(KB, alpha, symbols):
    print("KB entails alpha (TRUE)")
else:
    print("KB does not entail alpha (FALSE)")
