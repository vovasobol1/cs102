from unittest import TestCase
from src.lab4.num2 import Group, Groups, main


class CalculatorTestCase(TestCase):
    def test_Group(self) -> None:
        group = Group('aboba')
        for i in range(3):
            group.add_person(f'aboba{i ** 4}', i)
            group.add_person(f'aboba{i}', i)
        self.assertEqual(group.__repr__(), 'aboba: aboba16 (2), aboba2 (2), aboba1 (1), aboba1 (1), aboba0 (0), aboba0 (0)')

    def test_Groups(self) -> None:
        groups = Groups([10, 20, 30, 40])
        groups.add_person(f'aboba5', 5)
        for i in range(25, 51, 5):
            groups.add_person(f'aboba{i}', i)
        self.assertEqual(groups.__repr__(), '41+: aboba50 (50), aboba45 (45)\n31-40: aboba40 (40), aboba35 (35)\n'
                                            '21-30: aboba30 (30), aboba25 (25)\n0-10: aboba5 (5)')

    def test_main(self) -> None:
        self.assertEqual(main([18, 25, 35, 45, 60, 80, 100],
                              [['Кошельков Захар Брониславович', 105], ['Старостин Ростислав Ермолаевич', 50],
                               ['Дьячков Нисон Иринеевич', 88], ['Иванов Варлам Якунович', 88],
                               ['Соколов Андрей Сергеевич', 15], ['Егоров Алан Петрович', 7],
                               ['Ярилова Розалия Трофимовна', 29]]),
                         '101+: Кошельков Захар Брониславович (105)\n81-100: Дьячков Нисон Иринеевич (88), '
                         'Иванов Варлам Якунович (88)\n46-60: Старостин Ростислав Ермолаевич (50)\n'
                         '26-35: Ярилова Розалия Трофимовна (29)\n0-18: Соколов Андрей Сергеевич (15), '
                         'Егоров Алан Петрович (7)')
