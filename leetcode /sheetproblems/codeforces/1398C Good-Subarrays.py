from itertools import accumulate
from copy import deepcopy
from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, list(input())))
    prefix = list(accumulate(a))
    dict = defaultdict(int)
    dict[0] = 1
    res = 0
    for i in range(n):
        diff = prefix[i] - (i+1)
        dict[diff] += 1
        res += (dict[diff] - 1)
    print(res)