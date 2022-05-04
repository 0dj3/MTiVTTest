from main import Exam, Group, Specialization, Subject, Student
from datetime import date
from classes import institute
import unittest


class TestGetExam(unittest.TestCase):

    sp = Specialization("ФИИТ")
    gr = Group(sp, 2012)
    su = Subject("Б1.Б.22", "Основы программирования", 1, 144, sp)
    da = date(2018, 1, 10)
    ex = Exam(su, da, "2018-2019", "Эверстов Владимир Васильевич", gr)
    inst = institute.Institute()
    inst.add_exam(ex)

    def test_one(self):  # Корректное количество строк
        res = []
        res.append(self.inst.get_exam(self.gr.name,self.su.name,self.da))
        self.assertEqual(len(res), 1)


