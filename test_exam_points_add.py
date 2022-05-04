from main import ExamPoints, Student, Specialization, Group, Subject
from classes import institute
from datetime import date
import unittest


class TestAddExamPoints(unittest.TestCase):

    student = Student("Иннокентьев Владимир Евгеньевич", 172531)
    spec = Specialization("ФИИТ")
    subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
    group = Group(spec, 2021)
    d = date(2021, 1, 10)

    def test_one(self):  # Корректный тест
        ep = ExamPoints(self.student, 55.4, 30.0, self.d, self.group.name, self.subject)
        inst = institute.Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 1)

    def test_two(self):  # Ошибка в типе параметра student
        inst = institute.Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(1, 55.4, 30.0, self.d, self.group.name, self.subject)
            inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 0)

    def test_three(self):  # Ошибка в типе параметра inpoints
        inst = institute.Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(self.student, "55.4", 30.0, self.d, self.group.name, self.subject)
            inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 0)

    def test_four(self):  # Ошибка в типе параметра exampoints
        inst = institute.Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(self.student, 55.4, 30, self.d, self.group.name, self.subject)
            inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 0)

    def test_five(self):  # Ошибка в количестве баллов параметра inpoints > 70
        inst = institute.Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(self.student, 80.2, 30.0, self.d, self.group.name, self.subject)
            inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 0)

    def test_six(self):  # Ошибка в количестве баллов параметра inpoints < 0
        inst = institute.Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(self.student, -55.4, 30.0, self.d, self.group.name, self.subject)
            inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 0)

    def test_seven(self):  # Ошибка в количестве баллов параметра exampoints < 0
        inst = institute.Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(self.student, 55.4, -30.0, self.d, self.group.name, self.subject)
            inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 0)

    def test_eight(self):  # Ошибка в количестве баллов параметра exampoints > 30
        inst = institute.Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(self.student, 55.4, 31.0, self.d, self.group.name, self.subject)
            inst.add_exam_points(ep)
        self.assertEqual(len(inst.exam_points), 0)


if __name__ == "__main__":
    unittest.main()
