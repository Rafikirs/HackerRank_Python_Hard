# Exercise: Maximize It!
# URL: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Description: Finding the biggest modulo among the sum of squares of values picked randomly among different lists

from itertools import product

K, M = map(int, input().split())
lines = []

for _ in range(K):
    line = list(map(int, input().split()))[1:]
    lines.append(line) 
    
all_combis = list(product(*lines))

all_mods = sorted([sum(x**2 for x in combi)%M for combi in all_combis])

print(all_mods[-1])
