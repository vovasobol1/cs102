from typing import Union  # Импортируем Union для определения типов


class Group:  # Создаем класс группы людей
    def __init__(self, name) -> None:  # Инициализируем объект
        self.name = name  # Создаем имя группы
        self.group: dict[int, list[str]] = {}  # Создаем словарь с людьми (ключ - возраст, значение - имя)

    def add_person(self, name: str, age: int) -> None:  # Функция добавления человека
        if age in self.group:  # Если возраст уже ключ
            self.group[age].append(name)  # Добавляем имя по ключу
        else:  # Иначе
            self.group[age] = [name]  # Добавляем ключ со значением - списком с единственным именем

    def __repr__(self) -> str:  # Функция строкового представления класса
        ages = self.group.keys()  # Берем все возрасты
        if ages:  # Если словарь не пуст
            return f'{self.name}: ' + ', '.join([f' ({key}), '.join(sorted(self.group[key])) + f' ({key})'
                                                 for key in sorted(ages, reverse=True)])  # Возвращаем строку по формату
        return ''  # Иначе возвращаем пустую строку


class Groups:  # Класс нескольких групп
    def __init__(self, ages: list[int]) -> None:  # Инициализируем объект
        self.ages = ages  # Создаем список возрастов в группе
        self.groups = [Group(f'0-{ages[0]}')]  # Создаем список, первый элемент - группа самых маленьких
        for age in range(1, len(ages)):  # Проходимся по оставшимся возрастам
            self.groups.append(Group(f'{ages[age - 1] + 1}-{ages[age]}'))  # Добавляем группу каждого возраста
        self.groups.append(Group(f'{ages[-1] + 1}+'))  # Добавляем группу самых старых

    def add_person(self, name: str, age: int) -> None:  # Функция добавления человека
        if age > self.ages[-1]:  # Если возраст больше максимального
            self.groups[-1].add_person(name, age)  # Добавляем в группу самых старых
        elif age <= self.ages[0]:  # Если возраст меньше минимального
            self.groups[0].add_person(name, age)  # Добавляем в группу самых маленьких
        else:  # Иначе
            for i in range(1, len(self.ages)):  # Проходимся по всем возрастам
                if self.ages[i - 1] < age <= self.ages[i]:  # Если возраст лежит между двух каких-то
                    self.groups[i].add_person(name, age)  # Добавляем в группу по этому возрасту
                    break  # Прекращаем цикл прохода

    def __repr__(self) -> str:  # Функция строкового представления
        groups = []  # Создаем список групп
        for group in self.groups[::-1]:  # Проходимся по всем группам из наших
            people = group.__repr__()  # Берем строковое представление каждой группы
            if people:  # Если строковое представление непустое
                groups.append(people)  # Добавляем группу в список
        return '\n'.join(groups)  # Выводим строку из групп по формату


def main(ages: list[int], persons: list[list[Union[int, str]]]) -> str:  # Главная функция
    groups = Groups(ages)  # Создаем объект нескольких групп по возрасту
    for person in persons:  # Проходимся по всем людям
        groups.add_person(person[0], int(person[1]))  # Добавляем в объект человека
    return groups.__repr__()  # Возвращаем строковое представление


if __name__ == '__main__':  # Если файл запущен как главный
    ages = [int(age) for age in input().split()]  # Читаем возрасты с клавиатуры
    persons = []  # Создаем список людей
    person = input()  # Читаем строку
    while person != 'END':  # Пока строка не означает конец ввода
        person = person.split(',')  # Форматируем стркоу в список
        persons.append([person[0], int(person[1])])  # Добавляем в список людей человека: имя и возраст
        person = input()  # Читаем новую строку
    print(main(ages, persons))  # Выводим результат работы главной функции

'''
18 25 35 45 60 80 100
Кошельков Захар Брониславович,105
Старостин Ростислав Ермолаевич,50
Дьячков Нисон Иринеевич,88
Иванов Варлам Якунович,88
Соколов Андрей Сергеевич,15
Егоров Алан Петрович,7
Ярилова Розалия Трофимовна,29
END
'''