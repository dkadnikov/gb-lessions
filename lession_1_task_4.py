# Урок-1
# Задача-4

# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Решение-задачи-4
print("")
print("Решение-задачи-4")
print("")
a = int(input("Введите любое положительноце целое число - "))
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(f"Самая большая цифра в веденном числе - {m}")

