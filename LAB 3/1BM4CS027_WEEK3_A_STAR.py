import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# -----------------------------
# Manhattan Distance
# -----------------------------
def manhattan(state):
    h = 0

    for i in range(9):

        if state[i] == 0:
            continue

        goal_position = GOAL.index(state[i])

        r1, c1 = divmod(i, 3)
        r2, c2 = divmod(goal_position, 3)

        h += abs(r1 - r2) + abs(c1 - c2)

    return h


# -----------------------------
# Misplaced Tiles
# -----------------------------
def misplaced(state):
    h = 0

    for i in range(9):

        if state[i] != 0 and state[i] != GOAL[i]:
            h += 1

    return h


# -----------------------------
# Generate possible movements
# -----------------------------
def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row, col = divmod(zero, 3)

    moves = [
        (-1, 0, "Top"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, direction in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            # Move blank
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(
                (tuple(new_state), direction)
            )

    return neighbors


# -----------------------------
# Print puzzle
# -----------------------------
def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i],
              state[i + 1],
              state[i + 2])


# -----------------------------
# A* Search
# -----------------------------
def a_star(start, heuristic):

    # (f, g, state, path)
    pq = []

    h = heuristic(start)

    heapq.heappush(
        pq,
        (h, 0, start, [])
    )

    visited = set()

    while pq:

        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == GOAL:
            return path

        print("\n==============================")
        print("CURRENT STATE")
        print("==============================")

        print_puzzle(current)

        print("\nPossible Moves:")

        possible_moves = []

        # Find all possible moves
        for neighbor, direction in get_neighbors(current):

            if neighbor not in visited:

                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h

                possible_moves.append(
                    (new_f,
                     new_g,
                     new_h,
                     direction,
                     neighbor)
                )

        # Show every possible move
        for move in possible_moves:

            new_f, new_g, new_h, direction, neighbor = move

            print(
                direction,
                "-> g =",
                new_g,
                ", h =",
                new_h,
                ", f =",
                new_g,
                "+",
                new_h,
                "=",
                new_f
            )

        # Add to priority queue
        for move in possible_moves:

            new_f, new_g, new_h, direction, neighbor = move

            new_path = path + [
                (direction,
                 neighbor,
                 new_g,
                 new_h,
                 new_f)
            ]

            heapq.heappush(
                pq,
                (new_f,
                 new_g,
                 neighbor,
                 new_path)
            )

    return None


# ==========================================
# MAIN PROGRAM
# ==========================================

print("===================================")
print("       8 PUZZLE - A* SEARCH")
print("===================================")

print("\nEnter 0 for the blank space.")

start = tuple(
    map(int, input("Enter puzzle: ").split())
)

# Check input
if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid puzzle!")
    exit()


# -----------------------------
# Choose heuristic
# -----------------------------

print("\nChoose Heuristic:")
print("1. Manhattan Distance")
print("2. Misplaced Tiles")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":

    heuristic = manhattan
    print("\nYou selected: Manhattan Distance")

elif choice == "2":

    heuristic = misplaced
    print("\nYou selected: Misplaced Tiles")

else:

    print("Invalid choice!")
    exit()


# -----------------------------
# Display starting state
# -----------------------------

print("\nSTART STATE:")
print_puzzle(start)


# -----------------------------
# Run A*
# -----------------------------

solution = a_star(start, heuristic)


# -----------------------------
# Display final solution
# -----------------------------

if solution:

    print("\n\n===================================")
    print("          FINAL SOLUTION")
    print("===================================")

    for step, data in enumerate(solution, 1):

        direction, state, g, h, f = data

        print("\nStep", step)

        print("Movement :", direction)

        print("g(n) =", g)

        print("h(n) =", h)

        print("f(n) =", g, "+", h, "=", f)

        print("\nState:")

        print_puzzle(state)

    print("\nGoal Reached!")

    print("Total Cost =", len(solution))

else:

    print("\nNo solution found!")
