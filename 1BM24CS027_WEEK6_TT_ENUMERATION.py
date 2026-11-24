
def evaluate(expr, model):
    return eval(expr, {}, model)


def tt_check_all(kb, alpha, symbols, model):
    if not symbols:
        if evaluate(kb, model):
            return evaluate(alpha, model)
        return True

    p = symbols[0]
    rest = symbols[1:]

    model_true = model.copy()
    model_true[p] = True

    model_false = model.copy()
    model_false[p] = False

    return (tt_check_all(kb, alpha, rest, model_true)
            and tt_check_all(kb, alpha, rest, model_false))


def tt_entails(kb, alpha):
    symbols = sorted(set(
        kb.replace("and", "").replace("or", "")
          .replace("not", "").replace("(", "")
          .replace(")", "").replace(" ", "")
    ) | set(
        alpha.replace("and", "").replace("or", "")
             .replace("not", "").replace("(", "")
             .replace(")", "").replace(" ", "")
    ))

    print("\nTruth Table:")
    print("-" * 55)

    for s in symbols:
        print(f"{s:^8}", end="")
    print(f"{'KB':^12}{'Query':^12}")

    print("-" * 55)

    for i in range(2 ** len(symbols)):
        model = {}
        for j, s in enumerate(symbols):
            model[s] = bool((i >> (len(symbols)-1-j)) & 1)

        kb_value = evaluate(kb, model)
        alpha_value = evaluate(alpha, model)

        for s in symbols:
            print(f"{str(model[s]):^8}", end="")

        print(f"{str(kb_value):^12}{str(alpha_value):^12}")

    print("-" * 55)

    return tt_check_all(kb, alpha, symbols, {})


# Main Program
kb = input("Enter Knowledge Base: ")
alpha = input("Enter Query: ")

if tt_entails(kb, alpha):
    print("\nKB entails Query: TRUE")
else:
    print("\nKB entails Query: FALSE")
