from time import time
import random
from math import copysign

def init_population():
    result = []
    for i in xrange(1,5):
        item = []
        for j in xrange(0,22):
            item.append(random.choice([0,1]))
        result.append(item)
    return result
 
items = (
    ("map", 90, 150), ("compass", 130, 35), ("water", 1530, 200), ("sandwich", 500, 160),
    ("glucose", 150, 60), ("tin", 680, 45), ("banana", 270, 60), ("apple", 390, 40),
    ("cheese", 230, 30), ("beer", 520, 10), ("suntan cream", 110, 70), ("camera", 320, 30),
    ("t-shirt", 240, 15), ("trousers", 480, 10), ("umbrella", 730, 40),
    ("waterproof trousers", 420, 70), ("waterproof overclothes", 430, 75),
    ("note-case", 220, 80), ("sunglasses", 70, 20), ("towel", 180, 12),
    ("socks", 40, 50), ("book", 300, 10),
    )

combinations = init_population()

def fitness(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for index in range(0, len(comb)):
        totwt  += comb[index]*items[index][1]
        totval += comb[index]*items[index][2]
    return (totwt, totval) if totwt <= 5000 else (0, 0)

def crossover(first, second):
	point = 1 + random.randrange(len(first)-2)
        new_mask_1 = first[:point] + second[point:]
        new_mask_2 = second[:point] + first[point:]
	return new_mask_1, new_mask_2

def mutate(chromosome):
        point = random.randrange(len(chromosome))
        chromosome[point] = int( copysign(chromosome[point]-1, 1) )
        return chromosome    


def genetic(estimated_time):

    start_time = time()
    while  time() - start_time < estimated_time:
        first = random.randrange(0, len(combinations))
        second = random.randrange(0, len(combinations))
        new_first, new_second = crossover(combinations[first], combinations[second])
        mutate(new_first)
        mutate(new_second)
        combinations.append(new_first)
        combinations.append(new_second)
    values = [fitness(item)
                for item in combinations 
                if fitness(item)[0] <= 5000]
    return values.index(max(values, key=lambda item: (item[1], item[0])))
		
def print_solution(time):
    index = genetic(time)
    solution = combinations[index]
    print(solution)
    for i in xrange(0, len(solution)):
        if solution[i] == 1:
            print(items[i])

print_solution(3)
