# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict

company = defaultdict(list)

n = int(input("Количество предприятий: "))
total_profit = 0  # счетчик общей прибыли
quarter = 4  # кол-во кварталов

for i in range(n):
    company_profit = 0  # счетчик прибыли компании
    com_name = input(f'название {i + 1}-го предприятия: ')
    for j in range(quarter):
        point = int(input(f'введите прибыль компании {com_name} за {j + 1}-ый квартал: '))
        company_profit += point
        company[com_name].append(company_profit)
    total_profit += company_profit

print(company)
avrg = total_profit / n
print(f'\nСредняя прибыль всех предприятий за {quarter} квартала: {avrg}')
for i in company:
    if sum(company[i]) > avrg:
        print(f'У компании {i} прибыль выше среднего')
    elif sum(company[i]) < avrg:
        print(f'У компании {i} прибыль ниже среднего')
