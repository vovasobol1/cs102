from typing import Union  # Импортируем Union для определения типов


PATH_TO_INPUT1 = 'input1_1.txt'  # Задаем путь к первому файлу (по условию задачи он должен быть доступен к изменению)
PATH_TO_INPUT2 = 'input1_2.txt'  # Аналогично задаем путь ко второму файлу


class FilmsDB(dict):  # Создаем класс базы фильмов, наследующийся от словаря
    def __init__(self, films_dict: dict[int, str]) -> None:  # Инициализируем объект
        super().__init__()  # Инициализируем супер-класс словаря
        self.films = films_dict  # Задаем собственно нашу базу фильмов

    def get_film(self, id: int) -> str:  # Метод, возвращающий название фильма по его номеру
        try:  # Пробуем найти фильм
            return self.films[id]  # Если такой номер есть, возвращаем название
        except KeyError:  # Если номера нет
            return 'ERROR: film does not found!'  # Возвращаем строку, сообщающую об ошибке


class User(list):  # Создаем класс пользователя, наслудующийся от списка
    def __init__(self, user_films: list[int]) -> None:  # Инициализируем объект
        super().__init__()  # Инициализируем супер-класс списка
        self.films = user_films  # Создаем список номеров фильмов, просмотренных пользователем


def count_score(person: User, user: User) -> Union[int, list[Union[float, list[int]]]]:
    # Функция, считающая вес рекомендаций
    person_films = set(person.films)  # Переводим список фильмов пользователя, для которого ищем рекомендацию, и список
    user_films = set(user.films)  # фильмов другого пользователя в множество, чтобы убрать повторящиеся фильмы
    if 2 * len(person_films & user_films) >= len(user_films):
        # Если количество общих просмотренных фильмов не меньше половины другого
        return [len(person_films & user_films) / len(person_films), list(user_films - person_films)]
        # Возвращаем список, в нем первое - отношение количества элементов в пересечении множеств ко всему,
        # второе - непросмотренные фильмы
    return 0  # Иначе возвращаем вес 0


def algorithm(films: FilmsDB, users: list[User], person: User) -> str:  # Алгоритм, предлагающий фильм к просмотру
    normal_films = {}  # Задаем словарь нужных фильмов
    for user in users:  # Проходимся по всем пользователям
        score_user = count_score(person, user)  # Считаем вес рекомендаций
        if type(score_user) == list:  # Если наша рекомендация не 0
            for film in score_user[1]:  # Проходимся по всем рекомендованным фильмам
                if film in normal_films:  # Если фильм уже добавлен в словарь
                    normal_films[film] += score_user[0] * user.films.count(film)  # Увеличиваем вес на посчитанный
                else:  # Иначе
                    normal_films[film] = score_user[0] * user.films.count(film)  # Добавляем ключ с весом
    normal_films_list = [[film, normal_films[film]] for film in normal_films]  # Переводим словарь в список
    return films.get_film(sorted(normal_films_list, key=lambda x: x[1], reverse=True)[0][0])
    # Сортируем по убыванию веса рекомендации и возвращаем первое название фильма


if __name__ == '__main__':  # Если файл запущен как главный
    with open(PATH_TO_INPUT1, 'r', encoding='utf-8') as file1_input:  # Открываем первый файл
        films = {}  # Создаем словарь фильмов
        for line in file1_input.readlines():  # Проходимся по всем строкам файла
            film = line.strip().split(',')  # Разделяем строку по запятой (формат)
            films[int(film[0])] = film[1]  # Добавляем по номеру фильм в словарь
        films_db = FilmsDB(films)  # Создаем объект базы данных фильмов

    with open(PATH_TO_INPUT2, 'r', encoding='utf-8') as file2_input:  # Открываем второй файл
        users = []  # Создаем список пользователей
        for line in file2_input.readlines():  # Проходимся по строкам файла
            users.append(User(([int(film) for film in line.strip().split(',')])))
            # Добавляем в список пользователей класс User со списком фильмов

    person = User([int(film_id) for film_id in input().split(',')])
    # Читаем с клавиатуры просмотренные нашим пользователем фильмы и конвертируем в класс User
    print(algorithm(films_db, users, person))  # Выводим результат работы алгоритма
