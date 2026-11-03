
import random
import math

# Initial State
initial_state = [0, 1, 2, 3, 4, 5, 6, 7]

# Calculate diagonal conflicts (Cost Function)
def calculate_cost(state):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate neighboring state
def get_neighbor(state):
    new_state = state.copy()
    i, j = random.sample(range(8), 2)

    new_state[i], new_state[j] = new_state[j], new_state[i]

    return new_state


# Simulated Annealing
def simulated_annealing():

    current = initial_state.copy()

    T = 1000
    cooling_rate = 0.99

    while T > 0.001:

        current_cost = calculate_cost(current)

        # Goal test
        if current_cost == 0:
            return current

        # Generate next state
        next_state = get_neighbor(current)
        next_cost = calculate_cost(next_state)

        delta_E = current_cost - next_cost

        # Accept better state
        if delta_E > 0:
            current = next_state

        else:
            # Accept worse state with probability
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state

        # Decrease temperature
        T *= cooling_rate

    return current


# Display chessboard
def display_board(state):
    for row in range(8):
        for col in range(8):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


# Main Program

print("INITIAL STATE:")
print(initial_state)
print("Initial Cost:", calculate_cost(initial_state))
display_board(initial_state)

# State Space
print("\nSTATE SPACE:")
print("Total possible states =", math.factorial(8))

# Find solution
final_state = simulated_annealing()

print("\nFINAL STATE:")
print(final_state)

print("Final Cost:", calculate_cost(final_state))
display_board(final_state)

if calculate_cost(final_state) == 0:
    print("\nSolution Found!")
else:
    print("\nSolution not found. Run again.")
