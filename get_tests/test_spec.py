from main import Specialization
from classes import institute
from functions import getSpec
import unittest


class TestGetSpecialization(unittest.TestCase):

    sp = Specialization("ФИИТ")
    inst = institute.Institute()
    inst.add_spec(sp)

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.inst.get_spec(self.sp.name)), 1)

