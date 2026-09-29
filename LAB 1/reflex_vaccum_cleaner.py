#Find the code for reflex agent:
#Implementation of vaccum cleaner using simple reflex agent in python
# Program for Vacuum Cleaner with just 2 locations A and B
# Include the random module
import random

# Define the environment class
class Environment:
    def __init__(self):
        # Initialize the condition of locations A and B
        self.locationCondition = {'A': random.randint(0, 1), 'B': random.randint(0, 1)}

# Define the vacuum agent class that inherits from the Environment class
class SimpleReflexVacuumAgent:
    def __init__(self, environment):
        # Print the initial conditions of locations A and B
        print(environment.locationCondition)

        # Initialize the score
        score = 0

        # Randomly place the vacuum at location A (0) or B (1)
        vacuumLocation = random.randint(0, 1)

        if vacuumLocation == 0:
            print("Vacuum is randomly placed at Location A.")
            # Check if location A is dirty (1)
            if environment.locationCondition['A'] == 1:
                print("Location A is Dirty.")
                # Clean location A
                environment.locationCondition['A'] = 0
                score += 1
                print("Location A has been Cleaned.")
            else:
                print("Location A is Clean.")

            print("Moving to Location B...")
            # Check if location B is dirty (1)
            if environment.locationCondition['B'] == 1:
                print("Location B is Dirty.")
                # Clean location B
                environment.locationCondition['B'] = 0
                score += 1
                print("Location B has been Cleaned.")
            else:
                print("Location B is Clean.")

        else:
            print("Vacuum is randomly placed at Location B.")
            # Check if location B is dirty (1)
            if environment.locationCondition['B'] == 1:
                print("Location B is Dirty.")
                # Clean location B
                environment.locationCondition['B'] = 0
                score += 1
                print("Location B has been Cleaned.")
            else:
                print("Location B is Clean.")

            print("Moving to Location A...")
            # Check if location A is dirty (1)
            if environment.locationCondition['A'] == 1:
                print("Location A is Dirty.")
                # Clean location A
                environment.locationCondition['A'] = 0
                score += 1
                print("Location A has been Cleaned.")
            else:
                print("Location A is Clean.")

        # Print the final conditions of locations A and B
        print(environment.locationCondition)
        # Print the performance score
        print("Performance Measurement: " + str(score))

# Create an instance of the Environment class
theEnvironment = Environment()
# Create an instance of the SimpleReflexVacuumAgent class with the environment instance
theVacuum = SimpleReflexVacuumAgent(theEnvironment)