#!/usr/bin/env python3

import sys
import math
import itertools
from common import print_tour, read_input

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(cities, tour):
    distance = 0
    for i in range(len(tour)):
        distance += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    return distance

def solve(cities):
    n = len(cities)
    all_permutations = itertools.permutations(range(n))
    min_distance = float('inf')
    best_tour = None

    for perm in all_permutations:
        current_distance = total_distance(cities, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = perm

    return list(best_tour)

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
