import math
import timeit


def find_prime(pos):
    ind = 1
    simples = [2]
    cur = 3
    while ind < pos:
        rest = 0
        for d in simples:
            rest = cur % d
            if rest == 0:
                break
        if rest != 0:
            simples.append(cur)
            ind += 1
        cur += 2
    return simples[len(simples) - 1]


print(find_prime(10))
print(timeit.timeit('find_prime(10)', globals=globals(), number=100000))

print(find_prime(20))
print(timeit.timeit('find_prime(20)', globals=globals(), number=100000))

print(find_prime(40))
print(timeit.timeit('find_prime(40)', globals=globals(), number=100000))


def find_prime_re(pos):
    lim = math.ceil(2 * pos * math.log(pos))
    ma = list(range(2, lim))
    start_ind = 0
    cur_simple = 0
    res = 0
    while start_ind < len(ma):
        if ma[start_ind] != 0:
            cur_simple += 1
            if cur_simple == pos:
                res = ma[start_ind]
                break
            step = ma[start_ind]
            cur_pos = start_ind + step
            while cur_pos < len(ma):
                ma[cur_pos] = 0
                cur_pos += step
        start_ind += 1
    return res


print(find_prime_re(10))
print(timeit.timeit('find_prime_re(10)', globals=globals(), number=100000))
print(find_prime_re(20))
print(timeit.timeit('find_prime_re(20)', globals=globals(), number=100000))
print(find_prime_re(40))
print(timeit.timeit('find_prime_re(40)', globals=globals(), number=100000))

# 29
# 0.6340101
# 71
# 1.9487579999999998
# 173
# 6.395146
# 29
# 1.2755858
# 71
# 3.2944619
# 173
# 11.313060799999999

# Видимо не правильно реализовал второй алгоритм, хотя делал как понял.
# Нужно было определить верхню границу для i-го простого числа, нашел формулу 2*n*ln(n)



