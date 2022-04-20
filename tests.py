from main import Student, Specialization, Group, Subject, ExamPoints, Exam
from functions import getSubject
from datetime import date
import unittest


class TestClass(unittest.TestCase):
    def test_class_student(self):
        student = Student("Иннокентьев Владимир", 172531)
        self.assertEqual("Иннокентьев Владимир", student.fio)
        self.assertEqual(172531, student.code)

    def test_class_specialization(self):
        spec = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", spec.name)

    def test_class_group(self):
        spec = Specialization("ФИИТ")
        group = Group(spec, 2021)
        self.assertEqual("ФИИТ-21", group.name)
        self.assertEqual(spec, group.spec)
        self.assertEqual(2021, group.year)

    # def test_class_subject(self):
    #     subject = getSubject.getSubject(getSubject.importSubjects("data/subject.xlsx"), "Основы программирования")[0]
    #     spec = Specialization("ФИИТ")
    #     self.assertEqual("Б1.Б.22", subject.code)
    #     self.assertEqual("Основы программирования", subject.name)
    #     self.assertEqual(1, subject.semester)
    #     self.assertEqual(144, subject.hours)
    #     self.assertEqual(spec, subject.spec)

    def test_exam_points(self):
        spec = Specialization("ФИИТ")
        group = Group(spec, 2021)
        subj = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
        student = Student("Иннокентьев Владимир", 172531)
        d = date(2021, 1, 10)
        examPoints = ExamPoints(student, 55.4, 30.0, d, group.name, subj)
        self.assertEqual(student, examPoints.student)
        self.assertEqual(55.4, examPoints.inPoints)
        self.assertEqual(30.0, examPoints.examPoints)

    def test_exam(self):
        spec = Specialization("ФИИТ")
        group = Group(spec, 2021)
        subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
        d = date(2018, 1, 10)
        exam = Exam(subject, d, "2018-2019", "Эверстов Владимир Васильевич", group)
        self.assertEqual(subject, exam.subject)
        self.assertEqual(d, exam.examDate)
        self.assertEqual("2018-2019", exam.year)
        self.assertEqual("Эверстов Владимир Васильевич", exam.lectFio)


if __name__ == '__main__':
    unittest.main()
