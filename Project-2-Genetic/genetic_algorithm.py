
import random
import matplotlib.pyplot as plt # type: ignore

TARGET = "Hello CPSC 390!"
POPULATION_SIZE = 128
MUTATION_RATE = 0.09
ASCII_START = ord(' ')
ASCII_END = ord('z')
RUN_COUNT = 2

def generate_character():
    return chr(random.randint(ASCII_START, ASCII_END))

def generate_individual():
    return ''.join(generate_character() for _ in range(len(TARGET)))

def generate_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def fitness(candidate):
    fitness_counter = 0
    for c1, c2 in zip(candidate, TARGET):
        if c1 == c2:
            fitness_counter += 1
    return fitness_counter

def select_parents(population):
    population_sorted = sorted(population, key=fitness, reverse=True)
    parents = population_sorted[:POPULATION_SIZE // 2]
    return parents


def crossover(parent1, parent2):
    # combine the two parents to create a child
    child = ''
    for c1, c2 in zip(parent1, parent2):
        child += random.choice([c1, c2])
    return child


def mutate(child):
    for c in range(len(child)):
        if random.random() < MUTATION_RATE:
            child = child[:c] + generate_character() + child[c+1:]
    return child


def plot_best_fitness_per_generation(best_fitness_history):
    generations = list(range(1, len(best_fitness_history) + 1))

    plt.figure(figsize=(9, 5))
    plt.plot(generations, best_fitness_history, color="teal", linewidth=2)
    plt.xscale("log")
    plt.title("Best Fitness per Generation")
    plt.xlabel("Generation (log scale)")
    plt.ylabel("Best Fitness Score")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def run_genetic_algorithm():
    solved = False
    generation = 0
    initial_population = generate_population()
    best_fitness_history = []

    while not solved:
        generation += 1
        best_individual = max(initial_population, key=fitness)
        best_fitness_score = fitness(best_individual)
        best_fitness_history.append(best_fitness_score)

        parents = select_parents(initial_population)
        children = []

        # Print the best fitness every 10 generations
        if generation % 10 == 0 or generation == 1:
            print("Generation: " + str(generation) + " Best fitness: " + str(best_fitness_score))

        # Create children until we have enough to fill the population
        while len(children) < POPULATION_SIZE // 2:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)

            child = crossover(parent1, parent2)
            child = mutate(child)

            children.append(child)

        # Combine parents and children to create the new population
        initial_population = parents + children

        # Check if any individual in the population is a solution
        for individual in initial_population:
            if fitness(individual) == len(TARGET):
                print("Solution found: " + individual)
                print("Generation: " + str(generation) + "\n")
                solved = True
                break

    if RUN_COUNT == 1:
        plot_best_fitness_per_generation(best_fitness_history)

    return generation

if __name__ == "__main__":
    generation_count = []

    for i in range(RUN_COUNT):
        generation_count.append(run_genetic_algorithm())
    generation_count.sort()

    print("Average generations to solve: " + str(sum(generation_count) // len(generation_count)))
    print("Best: " + str(generation_count[0]) + " Worst: " + str(generation_count[-1]))

    print()
