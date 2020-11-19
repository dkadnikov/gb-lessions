# Урок-2
# Задача-5

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Решение-задачи-5
print("Решение-задачи-5")
print("")
first_rate = [7, 6, 5, 4, 3]
print(f"У меня есть рейтинг {first_rate}")
rate = int(input("Добавь свой, один, элемент рейтинга: "))

count = first_rate.count(rate)
for el in first_rate:
    if count > 0:
        i = first_rate(rate)
        first_rate.insert(i+count, rate)
        break
    else:
        if rate > el:
            n = first_rate.index(el)
            first_rate.insert(n, rate)
            break
        elif rate < first_rate[len(first_rate)-1]:
            first_rate.append(rate)
print(f"Я сделал обратный порядок рейтига и добавил в рейтинг твой элемент. Вот что вышло -  {first_rate} ")
