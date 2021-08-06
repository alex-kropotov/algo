# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
import collections

biz = collections.namedtuple('name', ['p1', 'p2', 'p3', 'p4', 'p_sum'])

biz_list = {}

qty = int(input("Введите количество предприятий: "))

for _ in range(qty):
    name, p1, p2, p3, p4 = \
        input('Введите через пробел, наименование предприятия и 4 числа прибыли за 4 квартала: ').split(' ')
    biz_list[name] = biz(p1=float(p1), p2=float(p2), p3=float(p3), p4=float(p4),
                         p_sum=float(p1) + float(p2) + float(p3) + float(p4))
p_sum = 0

for _, prof in biz_list.items():
    p_sum += prof.p_sum
p_avg = p_sum / qty


print('Предприятия, у которых прибыль выше среднего:')
for name, prof in biz_list.items():
    if prof.p_sum > p_avg:
        print(name)

print('Предприятия, у которых прибыль ниже среднего:')
for name, prof in biz_list.items():
    if prof.p_sum < p_avg:
        print(name)
