from main import Student
from classes import institute
import unittest


class TestAddStudent(unittest.TestCase):
    def test_one(self):  # Корректный тест
        stud = Student("Иннокентьев Владимир Евгеньевич", 175351)
        inst = institute.Institute()
        inst.add_student(stud)
        self.assertEqual(len(inst.students), 1)

    def test_two(self):  # Ошибка из-за неправильного ФИО
        inst = institute.Institute()
        with self.assertRaises(Exception):
            stud = Student("НюхачБебры", 175351)
            inst.add_student(stud)
        self.assertEqual(len(inst.students), 0)

    def test_three(self):  # Ошибка из-за пустого ФИО
        inst = institute.Institute()
        with self.assertRaises(Exception):
            stud = Student("", 175351)
            inst.add_student(stud)
        self.assertEqual(len(inst.students), 0)

    def test_four(self):  # Ошибка неправильного типа параметра fio
        inst = institute.Institute()
        with self.assertRaises(Exception):
            stud = Student(1, 175351)
            inst.add_student(stud)
        self.assertEqual(len(inst.students), 0)

    def test_five(self):  # Ошибка неправильного типа параметра code
        inst = institute.Institute()
        with self.assertRaises(Exception):
            stud = Student("Иннокентьев Владимир Евгеньевич", "175351")
            inst.add_student(stud)
        self.assertEqual(len(inst.students), 0)

    def test_six(self):  # Ошибка при добавлении неправильного типа
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_student(1)
        self.assertEqual(len(inst.students), 0)

    def test_seven(self):  # Проверка на повтороный ввод (Одинаковые)
        stud = Student("Иннокентьев Владимир Евгеньевич", 175351)
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_student(stud)
            inst.add_student(stud)
        self.assertEqual(len(inst.students), 1)

    def test_eight(self):  # Проверка на повтороный ввод (Одинаковые номера)
        stud = Student("Иннокентьев Владимир Евгеньевич", 175351)
        stud1 = Student("Евгеньев Иннокентий Владимирович", 175351)
        inst = institute.Institute()
        with self.assertRaises(Exception):
            inst.add_student(stud)
            inst.add_student(stud1)
        self.assertEqual(len(inst.students), 1)

    def test_nine(self):  # Проверка на повтороный ввод (Корректный)
        stud = Student("Иннокентьев Владимир Евгеньевич", 175351)
        stud1 = Student("Евгеньев Иннокентий Владимирович", 175352)
        inst = institute.Institute()
        inst.add_student(stud)
        inst.add_student(stud1)
        self.assertEqual(len(inst.students), 2)


if __name__ == "__main__":
    unittest.main()
