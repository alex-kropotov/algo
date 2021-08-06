# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ
#
# В сети есть алгоритмы получше, но не стреляйте в тапера, он играет как умеет


from collections import deque

hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

dec_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
              10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# перемножение двух одноразрядных шестнадцатиричных чисел
# возвращает словарь из двух чисел, 'l' - стапрший разряд, 'r' младший разряд
def single_hex_mul(x, y):
    dec_prod = hex_to_dec[x] * hex_to_dec[y]
    return {
        'l': dec_to_hex[dec_prod // 16],
        'r': dec_to_hex[dec_prod % 16],
    }


# сложение двух одноразрядных шестнадцатиричных чисел
# возвращает словарь из двух чисел, 'l' - стапрший разряд, 'r' младший разряд
# моэно было пожалуй обойтись без этой функции, но подумал - пусть будет
def single_hex_add(x, y):
    dec_prod = hex_to_dec[x] + hex_to_dec[y]
    return {
        'l': dec_to_hex[dec_prod // 16],
        'r': dec_to_hex[dec_prod % 16],
    }


# сложение двух шестнадцатеричных чисел, представленных двумя коллекциями типа deque
def deque_hex_add(d1_i, d2_i):
    d1 = d1_i
    d2 = d2_i
    if len(d1) > len(d2):
        for _ in range((len(d1) - len(d2))):
            d2.appendleft('0')
    elif len(d2) > len(d1):
        for _ in range((len(d2) - len(d1))):
            d1.appendleft('0')
    result = deque()
    sh = '0'
    for _ in range(len(d1)):
        t1 = single_hex_add(d1.pop(), d2.pop())
        t2 = single_hex_add(t1['r'], sh)
        result.appendleft(t2['r'])
        sh = '1' if t1['l'] == '1' or t2['l'] == '1' else '0'
    if sh == '1':
        result.appendleft('1')
    # test
    # print(deque_hex_add(deque(list('6754AEF2'.upper())), deque(list('456da7'.upper())))) ==
    # deque(['6', '7', '9', 'A', '1', 'C', '9', '9'])
    return result


# умножение одноразрядноного s на очередь d с возможным сдвигом на n разрядов
def deque_single_hex_mul(d_i, s, n):
    d = deque(d_i)
    res = deque()
    add = '0'
    for _ in range(len(d)):
        # складываем два одноразрядных, получим или одноразрядное или двух
        t = single_hex_mul(d.pop(), s)
        # к младшему разряду прибавим то, что пришло с предыдущего шага,
        # можем получить двухразрядное
        t1 = single_hex_add(t['r'], add)
        # с младшим разрядом понятно, записываем его в результат
        res.appendleft(t1['r'])
        # а здесь может приехать переполнение и из первого сложения и из второго
        t2 = single_hex_add(t['l'], t1['l'])
        # но мы ожидаем что тут только ммладщий разряд будет в любом случае
        add = t2['r']
    # когда все прошли, допишем слева что осталось, если там не 0
    if add != '0':
        res.appendleft(add)
    # сдвигаем если n > 0
    while n > 0:
        res.append('0')
        n -= 1
    # надеемся что получили что нужно
    # и странно, но так и есть
    # deque_single_hex_mul(deque(list('6754AEF2'.upper())), 'A', 1) ==
    # deque(['4', '0', '9', '4', 'E', 'D', '5', '7', '4', '0'])
    return res


# финальная целевая функция
def mul(d1_i, d2):
    d1 = deque(d1_i)
    start = True
    for i in range(len(d2)):
        d = d2.pop()
        middle = deque_single_hex_mul(d1, d, i)
        if start:
            res = middle
            start = False
        else:
            res = deque_hex_add(res, middle)
    return res


first = deque(list('6754AEF2'.upper()))
second = deque(list('456da7'.upper()))


print(mul(first, second))

# проверил по калькулятору
# deque(['1', 'C', '0', '6', '1', '5', '9', 'D', 'F', '5', '2', '9', 'D', 'E'])


