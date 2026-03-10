
import random

TARGET = "Hello CPSC 390!"
POPULATION_SIZE = 128
MUTATION_RATE = 0.09
ASCII_START = ord(' ')
ASCII_END = ord('z')
RUN_COUNT = 1

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


def run_genetic_algorithm():
    solved = False
    generation = 0
    initial_population = generate_population()

    while not solved:
        generation += 1

        parents = select_parents(initial_population)
        children = []

        # Print the best fitness every 10 generations
        if generation % 10 == 0 or generation == 1:
            print("Generation: " + str(generation) + " Best fitness: " + str(fitness(initial_population[0])))

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
                print("Generation: " + str(generation))
                solved = True
                break
    
    return generation

if __name__ == "__main__":
    generation_count = []

    for i in range(RUN_COUNT):
        generation_count.append(run_genetic_algorithm())
    generation_count.sort()

    print()

    print("Average generations to solve: " + str(sum(generation_count) // len(generation_count)))
    print("Best: " + str(generation_count[0]) + " Worst: " + str(generation_count[-1]))

    print()

