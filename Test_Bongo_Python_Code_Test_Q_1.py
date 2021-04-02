import Bongo_Python_Code_Test_Q_1
import unittest

a = {
    'key1': 1,
    'key2':
        {
            'key3': 1,
            'key4': 2,
            'key5':
                {
                    'key6': 3,
                    'key7': 5,
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


class Test_Q1(unittest.TestCase):

    def test_depth(self):
        result_a = Bongo_Python_Code_Test_Q_1.dict_depth(a, depth=1)
        self.assertEqual(result_a, 3)
