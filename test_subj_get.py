from main import Subject, Specialization
from classes import institute
import unittest


class TestGetSubject(unittest.TestCase):

    spec = Specialization("ФИИТ")
    subj = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
    inst = institute.Institute()
    inst.add_subj(subj)

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.inst.get_subject(self.subj.name)), 1)


