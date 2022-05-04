from main import Group, Specialization
from classes import institute
import unittest


class TestAddGroup(unittest.TestCase):
    def test_one(self):  # Корректный тест
        sp = Specialization("ФИИТ")
        gr = Group(sp, 2012)
        inst = institute.Institute()
        inst.add_group(gr)
        self.assertEqual(len(inst.groups), 1)

    def test_two(self):  # Ошибка в типе параметра year
        inst = institute.Institute()
        with self.assertRaises(Exception):
            sp = Specialization("ФИИТ")
            gr = Group(sp, "2012")
            inst.add_group(gr)
        self.assertEqual(len(inst.groups), 0)

    def test_three(self):  # Ошибка в типе параметра spec
        inst = institute.Institute()
        with self.assertRaises(Exception):
            gr = Group(1, 2012)
            inst.add_group(gr)
        self.assertEqual(len(inst.groups), 0)

    def test_four(self):  # Ошибка при пустом вводе
        inst = institute.Institute()
        with self.assertRaises(Exception):
            gr = Group()
            inst.add_group(gr)
        self.assertEqual(len(inst.groups), 0)

    def test_five(self):  # Проверка на повтороный ввод (Одинаковые)
        sp = Specialization("ФИИТ")
        gr = Group(sp, 2012)
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_group(gr)
            inst.add_group(gr)
        self.assertEqual(len(inst.groups), 1)

    def test_six(self):  # Проверка на повтороный ввод (Корректный)
        sp = Specialization("ФИИТ")
        gr = Group(sp, 2012)
        gr1 = Group(sp, 2020)
        inst = institute.Institute()
        inst.add_group(gr)
        inst.add_group(gr1)
        self.assertEqual(len(inst.groups), 2)

    def test_seven(self):  # Ошибка при добавлении другого типа
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_group(1)
        self.assertEqual(len(inst.groups), 0)


if __name__ == '__main__':
    unittest.main()
