import random

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Generate a solvable initial state
def generate_state(moves=10):
    state = list(GOAL)
    previous = -1

    for _ in range(moves):

        zero = state.index(0)
        row, col = divmod(zero, 3)

        possible = []

        if row > 0:
            possible.append(zero - 3)      # Up

        if row < 2:
            possible.append(zero + 3)      # Down

        if col > 0:
            possible.append(zero - 1)      # Left

        if col < 2:
            possible.append(zero + 1)      # Right

        # Avoid immediately reversing the previous move
        if previous in possible and len(possible) > 1:
            possible.remove(previous)

        new_zero = random.choice(possible)

        state[zero], state[new_zero] = \
            state[new_zero], state[zero]

        previous = zero

    return tuple(state)


# Display puzzle
def display(state):
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x)
                       for x in state[i:i+3]))
    print()


# Generate neighbouring states
def get_neighbors(state):

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = []

    if row > 0:
        moves.append(zero - 3)      # Up

    if row < 2:
        moves.append(zero + 3)      # Down

    if col > 0:
        moves.append(zero - 1)      # Left

    if col < 2:
        moves.append(zero + 1)      # Right

    neighbors = []

    for new_zero in moves:

        new_state = list(state)

        new_state[zero], new_state[new_zero] = \
            new_state[new_zero], new_state[zero]

        neighbors.append(tuple(new_state))

    return neighbors


# Depth-Limited DFS
def depth_limited_dfs(state, goal, depth, path):

    # Goal found
    if state == goal:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    for new_state in get_neighbors(state):

        # Avoid cycles in current path
        if new_state not in path:

            result = depth_limited_dfs(
                new_state,
                goal,
                depth - 1,
                path + [new_state]
            )

            if result is not None:
                return result

    return None


# IDFS
def idfs(start, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        result = depth_limited_dfs(
            start,
            goal,
            depth,
            [start]
        )

        if result is not None:
            return result

        depth += 1


# ---------------- MAIN PROGRAM ----------------

# Automatically generate input
initial = generate_state(8)

print("INITIAL STATE:")
display(initial)

print("GOAL STATE:")
display(GOAL)

# Solve using IDFS
solution = idfs(initial, GOAL)

print("\nSOLUTION FOUND!")
print("Number of moves:", len(solution) - 1)
print()

for i, state in enumerate(solution):

    print("Step", i)
    display(state)