from main import Student
from classes import institute
import unittest


class TestGetStudent(unittest.TestCase):

    stud = Student("Иннокентьев Владимир Евгеньевич", 175351)
    inst = institute.Institute()
    inst.add_student(stud)

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.inst.get_student(self.stud.code)), 1)

