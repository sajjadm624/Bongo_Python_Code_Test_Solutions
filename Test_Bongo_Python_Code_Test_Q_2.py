import Bongo_Python_Code_Test_Q_2
import unittest


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            'user': person_b,
        }
    }
}

b = {
    'key1': 1,
    'key2':
        {
            'key3': 1,
            'key4': 2
        }
}


class Test_Q2(unittest.TestCase):

    def test_depth(self):
        result_a = Bongo_Python_Code_Test_Q_2.dict_depth(a, depth=1)
        result_b = Bongo_Python_Code_Test_Q_2.obj_depth(a, depth=1)
        self.assertEqual(result_a, 2)
        self.assertEqual(result_b, 4)
