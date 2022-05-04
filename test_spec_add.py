from main import Specialization
from classes import institute
import unittest


class TestAddSpec(unittest.TestCase):
    def test_one(self):  # Корректный тест
        sp = Specialization("ФИИТ")
        inst = institute.Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_two(self):  # Ошибка в типе параметра name
        inst = institute.Institute()
        with self.assertRaises(Exception):
            sp = Specialization(12)
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 0)

    def test_three(self):  # Ошибка из-за пустой строки в name
        inst = institute.Institute()
        with self.assertRaises(Exception):
            sp = Specialization("")
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 0)

    def test_four(self):  # Ошибка из-за пустого name
        inst = institute.Institute()
        with self.assertRaises(Exception):
            sp = Specialization()
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 0)

    def test_five(self):  # Проверка на повтороный ввод (Одинаковые)
        sp = Specialization("ФИИТ")
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_six(self):  # Проверка на повтороный ввод (Корректный)
        sp = Specialization("ФИИТ")
        sp1 = Specialization("ИВТ")
        inst = institute.Institute()
        inst.add_spec(sp)
        inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)

    def test_seven(self):  # Ошибка при добавлении другого типа
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_spec(1)
        self.assertEqual(len(inst.specs), 0)


if __name__ == '__main__':
    unittest.main()
