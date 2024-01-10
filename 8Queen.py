import random

# Number of queens
nq = 8


# Function to generate a random chromosome
def random_chromosome():
    chromosome = []
    for _ in range(nq):
        chromosome.append(random.randint(1, nq))
    return chromosome


# Function to calculate the fitness of a chromosome
def fitness(chromosome):
    horizontal_collisions = 0
    for queen in chromosome:
        queen_count = chromosome.count(queen)
        if queen_count > 1:
            horizontal_collisions += queen_count - 1
    horizontal_collisions = horizontal_collisions / 2

    diagonal_collisions = 0
    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(horizontal_collisions + diagonal_collisions)


# Generate 15 random chromosomes
population = []
for _ in range(15):
    population.append(random_chromosome())

# Calculate fitness scores for all chromosomes
fitness_scores = []
for chromosome in population:
    fitness_scores.append(fitness(chromosome))
