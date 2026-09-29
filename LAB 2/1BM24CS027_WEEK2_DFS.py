import random

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Generate a solvable initial state
def generate_state(moves=10):
    state = list(GOAL)

    for _ in range(moves):
        zero = state.index(0)
        row, col = divmod(zero, 3)

        possible = []

        if row > 0:
            possible.append(zero - 3)     # Up
        if row < 2:
            possible.append(zero + 3)     # Down
        if col > 0:
            possible.append(zero - 1)     # Left
        if col < 2:
            possible.append(zero + 1)     # Right

        new_zero = random.choice(possible)

        state[zero], state[new_zero] = \
            state[new_zero], state[zero]

    return tuple(state)


# Print puzzle
def display(state):
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x)
                       for x in state[i:i+3]))
    print()


# DFS algorithm
def dfs(start, goal):

    # Stack contains (state, path)
    stack = [(start, [start])]
    visited = set()

    while stack:

        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        # Position of blank
        zero = state.index(0)
        row, col = divmod(zero, 3)

        # Generate possible moves
        moves = []

        if row > 0:
            moves.append(zero - 3)     # Up

        if row < 2:
            moves.append(zero + 3)     # Down

        if col > 0:
            moves.append(zero - 1)     # Left

        if col < 2:
            moves.append(zero + 1)     # Right

        # Generate new states
        for new_zero in moves:

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                stack.append((new_state, path + [new_state]))

    return None


# ---------------- MAIN ----------------

# Automatically generate initial state
initial = generate_state(8)

print("INITIAL STATE:")
display(initial)

print("GOAL STATE:")
display(GOAL)

# Solve using DFS
solution = dfs(initial, GOAL)

if solution:

    print("SOLUTION FOUND")
    print("Number of moves:", len(solution) - 1)
    print()

    for i, state in enumerate(solution):
        print("Step", i)
        display(state)

else:
    print("NO SOLUTION")