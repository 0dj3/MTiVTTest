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
        self.assertEqual(len(inst.get_exam_points(self.group.name,self.subject.name,self.d)), 1)


if __name__ == "__main__":
    unittest.main()
