# Урок-3
# Задача-2

# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


# Решение-задачи-2
print("Решение-задачи-2")
print("")

def intro(**data) -> None:
    print(f'| Имя: {data.get("firstname")}, '
          f'| Фамилия: {data.get("lastname")} '
          f'| Год рождения: {data.get("birth_year")} '
          f'| Город: {data.get("city")} '
          f'| Электронная почта: {data.get("email")} '
          f'| Телефон: {data.get("telephone")} |')

if __name__ == '__main__':
    user = {
        'firstname': 'Лилу',
        'lastname': 'Даллас',
        'birth_year': '1990',
        'city': 'Illianopolis',
        'email': 'lily@incorp.com',
        'telephone': '+10000000000'
    }

    intro(**user)
