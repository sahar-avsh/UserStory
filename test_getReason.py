import unittest
from reason import getReason


class TestGetReason(unittest.TestCase):

    def test_single_verb_no_error(self):
        self.assertEqual(getReason(reason='save time'), ('save time', False))

    def test_single_verb_no_noun(self):
        with self.assertRaises(Exception) as context:
            getReason(reason='save')

        self.assertTrue('Reason must either consist a verb and a noun or an auxiliary verb and an adjective to be '
                        'meaningful.' in str(context.exception))

    def test_multiple_verbs(self):
        with self.assertRaises(Exception) as context:
            getReason(reason='save and spend money')

        self.assertTrue('Reason must include single item.' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
