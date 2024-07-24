import random

genome_length = 20
population_size = 100
mutation_rate = 0.01
crossover_rate = 0.7
generations = 200

def random_genome(length):
    return [random.choice([0, 1]) for _ in range(length)]

def init_population(pop_size, genome_length):
    return [random_genome(genome_length) for _ in range(pop_size)]

def fitness(genome):
    return sum(genome)

def select_parents(population, fitnesses): 
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)

    current = 0

    for individual,fitness in zip(population,fitnesses):
        current += fitness
        if current > pick:
            return individual
        
def crossover(p1, p2):
    if random.random() < crossover_rate:
        point = random.randint(1, len(p1)-1)
        return p1[:point] + p2[point:], p2[:point] + p1[point:]
    else:
        return p1, p2
    
def mutate(genome):
    for i in range(len(genome)):
        if random.random() < mutation_rate:
            genome[i] = 1 if genome[i] == 0 else 0

    return genome

def genetic_algorithm():
    population = init_population(population_size, genome_length)

    for generation in range(generations):
        fitnesses = [fitness(genome) for genome in population]

        next_generation = []

        for _ in range(population_size // 2):
            p1 = select_parents(population, fitnesses)
            p2 = select_parents(population, fitnesses)

            c1, c2 = crossover(p1, p2)

            next_generation.extend([mutate(c1), mutate(c2)])

        population = next_generation

        fitnesses = [fitness(genome) for genome in population]
        best_fitness = max(fitnesses)
        print(f"Generation {generation}: Best fitness {best_fitness}")

    best_index = fitnesses.index(max(fitnesses))
    best_solution = population[best_index]

    print(f"Best solution: {best_solution}")
    print(f"Best fitness: {fitness(best_solution)}")

if __name__ == "__main__":
    genetic_algorithm()