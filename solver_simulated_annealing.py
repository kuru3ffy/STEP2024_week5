#!/usr/bin/env python3

import sys
import math
import random
from common import print_tour, read_input

def calculate_distance(city1, city2):
    """
    2つの都市間のユークリッド距離を計算する関数。
    input:
        city1: 都市の座標 (x, y)
        city2: 都市の座標 (x, y)
    output:
        distance: 二つの都市の間の距離
    """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(cities, tour):
    """
    全都市間の総距離を計算する関数。
    input:
        cities: 都市の座標のリスト
        tour: 都市の巡回順序
    output:
        distance: 総距離
    """
    distance = 0
    for i in range(len(tour)):
        distance += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    return distance

def simulated_annealing(cities):
    """
    シミュレーテッド・アニーリングアルゴリズムを使用してTSPの解を求める関数
    input:
        cities: 都市の座標のリスト
    output: 
        best_tour: 最小距離を持つ巡回方法のリスト
    """
    n = len(cities)
    
    # 初期の都市の順番
    current_tour = list(range(n))
    current_distance = total_distance(cities, current_tour)
    
    # 温度設定
    temperature = 10000
    cooling_rate = 0.995
    min_temperature = 1e-10
    
    # 最良解の初期設定
    best_tour = current_tour[:]
    best_distance = current_distance

    while temperature > min_temperature:
        # 隣接解の生成
        new_tour = current_tour[:]
        i, j = random.sample(range(n), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        new_distance = total_distance(cities, new_tour)
        
        # 受容確率の計算
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_tour = new_tour
            current_distance = new_distance
            
            # 最良解の更新
            if new_distance < best_distance:
                best_tour = new_tour[:]
                best_distance = new_distance
        
        # 温度の低下
        temperature *= cooling_rate
    
    return best_tour

def solve(cities):
    """
    シミュレーテッド・アニーリングアルゴリズムを呼び出して、TSPの解を求める関数。
    input: 
        cities: 都市の座標のリスト
    output:
        simulated_annealing(cities): 最良の巡回方法
    """
    return simulated_annealing(cities)

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
