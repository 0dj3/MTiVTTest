from main import Group, Specialization
from classes import institute
import unittest


class TestGetGroup(unittest.TestCase):

    spec = Specialization("ФИИТ")
    group = Group(spec,2021)
    inst = institute.Institute()
    inst.add_group(group)

    def test_one(self):  # Корректное количество строк
        self.assertEqual(len(self.inst.get_group(self.group.name)), 1)



