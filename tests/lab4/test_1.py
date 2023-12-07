from unittest import TestCase
from src.lab4.num1 import FilmsDB, User, count_score, algorithm, PATH_TO_INPUT1, PATH_TO_INPUT2


class CalculatorTestCase(TestCase):
    def test_FilmsDB(self) -> None:
        self.assertEqual(FilmsDB({1: 'aboba', 3: 'aboba2', 17: 'aboba3'}).films,
                         {1: 'aboba', 3: 'aboba2', 17: 'aboba3'})

    def test_User(self) -> None:
        self.assertEqual(User([1, 6, 7, 4, 5, 6, 1]).films, [1, 6, 7, 4, 5, 6, 1])

    def test_count_score(self) -> None:
        self.assertEqual(count_score(User([1, 3, 4]), User([1, 2, 3, 4])), [1, [2]])

    def test_algorithm(self) -> None:
        self.assertEqual(algorithm(FilmsDB({i: f'aboba{i}' for i in range(1, 8)}),
                                   [User([1, 2, 3]), User([1, 2, 3]), User([3, 7]), User([1, 2, 7, 7, 7, 5])],
                                   User([1, 2, 3])), 'aboba7')
