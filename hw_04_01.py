from random import randint
import timeit


def f2(a):
    min_e = float('inf')
    max_e = float('-inf')
    for e in a:
        min_e = e if e < min_e else min_e
        max_e = e if e > max_e else max_e
    for idx, e in enumerate(a):
        a[idx] = max_e if e == min_e else (min_e if e == max_e else e)
    return a


a100 = [randint(-100, 100) for n1 in range(100)]
a200 = [randint(-200, 200) for n2 in range(200)]
a300 = [randint(-300, 300) for n3 in range(300)]


print(timeit.timeit('f2(a100)', globals=globals()))     # 19.445062
print(timeit.timeit('f2(a200)', globals=globals()))     # 41.943428600000004
print(timeit.timeit('f2(a300)', globals=globals()))     # 63.8597697

# можно сделать вывод что сложность алгоритма O(n), т.е. пропорциональна размеру входного массива

