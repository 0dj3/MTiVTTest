from main import Specialization, Subject
from classes import institute
import unittest


class TestAddSubj(unittest.TestCase):
    def test_one(self):  # Корректный тест
        spec = Specialization("ФИИТ")
        subj = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
        inst = institute.Institute()
        inst.add_subj(subj)
        self.assertEqual(len(inst.subjects), 1)

    def test_two(self):  # Ошибка в типе параметра code
        inst = institute.Institute()
        with self.assertRaises(Exception):
            spec = Specialization("ФИИТ")
            subj = Subject(1, "Основы программирования", 1, 144, spec)
            inst.add_subj(subj)
        self.assertEqual(len(inst.subjects), 0)

    def test_three(self):  # Ошибка в типе параметра name
        inst = institute.Institute()
        with self.assertRaises(Exception):
            spec = Specialization("ФИИТ")
            subj = Subject("Б1.Б.22", 1, 1, 144, spec)
            inst.add_subj(subj)
        self.assertEqual(len(inst.subjects), 0)

    def test_four(self):  # Ошибка в типе параметра semester
        inst = institute.Institute()
        with self.assertRaises(Exception):
            spec = Specialization("ФИИТ")
            subj = Subject("Б1.Б.22", "Основы программирования", "asd", 144, spec)
            inst.add_subj(subj)
        self.assertEqual(len(inst.subjects), 0)

    def test_five(self):  # Ошибка в типе параметра hours
        inst = institute.Institute()
        with self.assertRaises(Exception):
            spec = Specialization("ФИИТ")
            subj = Subject("Б1.Б.22", "Основы программирования", 1, "144", spec)
            inst.add_subj(subj)
        self.assertEqual(len(inst.subjects), 0)

    def test_six(self):  # Ошибка в типе параметра specialization
        inst = institute.Institute()
        with self.assertRaises(Exception):
            subj = Subject("Б1.Б.22", "Основы программирования", 1, 144, 1)
            inst.add_subj(subj)
        self.assertEqual(len(inst.subjects), 0)

    def test_seven(self):  # Ошибка при добавлении другого типа
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_subj(1)
        self.assertEqual(len(inst.subjects), 0)

    def test_eight(self):  # Проверка на повтороный ввод (Одинаковые)
        spec = Specialization("ФИИТ")
        subj = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_subj(subj)
            inst.add_subj(subj)
        self.assertEqual(len(inst.subjects), 1)

    def test_nine(self):  # Проверка на повтороный ввод (Корректно)
        spec = Specialization("ФИИТ")
        spec1 = Specialization("ИВТ")
        subj = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
        subj1 = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec1)
        inst = institute.Institute()
        inst.add_subj(subj)
        inst.add_subj(subj1)
        self.assertEqual(len(inst.subjects), 2)


if __name__ == "__main__":
    unittest.main()