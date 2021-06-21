import unittest
from demand import getDemand


class TestGetDemand(unittest.TestCase):

    def test_single_word_single_verb(self):
        self.assertEqual(getDemand(demand='sell'), ['sell'])

    def test_multiple_words_single_verb_1(self):
        self.assertEqual(getDemand(demand='sell online'), ['sell online'])

    def test_multiple_words_single_verb_2(self):
        self.assertEqual(getDemand(demand='selling online'), ['sell online'])

    def test_single_word_no_verb_1(self):
        with self.assertRaises(Exception) as context:
            getDemand(demand='Dog')

        self.assertTrue('Demand must start with a verb, "not" or "to".' in str(context.exception))

    def test_single_word_no_verb_2(self):
        with self.assertRaises(Exception) as context:
            getDemand(demand='For')

        self.assertTrue('Demand must start with a verb, "not" or "to".' in str(context.exception))

    def test_multiple_words_no_verb(self):
        with self.assertRaises(Exception) as context:
            getDemand(demand='Dog bed')

        self.assertTrue('Demand must start with a verb, "not" or "to".' in str(context.exception))

    def test_multiple_words_wrong_verb_place(self):
        with self.assertRaises(Exception) as context:
            getDemand(demand='Dog bed selling')

        self.assertTrue('Demand must start with a verb, "not" or "to".' in str(context.exception))

    def test_multiple_words_multiple_verbs_1(self):
        self.assertEqual(getDemand(demand='drink water and juice'), ['drink water', 'drink juice'])

    def test_multiple_words_multiple_verbs_2(self):
        self.assertEqual(getDemand(demand='drink water and buy juice'), ['drink water', 'buy juice'])

    def test_atomic_error(self):
        self.assertEqual(getDemand(demand='drink water and not buy juice'), ['drink water', 'not buy juice'])

    def test_minimal_error(self):
        with self.assertRaises(Exception) as context:
            getDemand(demand='producing (in-house) dog beds')

        self.assertTrue('Please do not specify anything more than a demand to keep requirement minimal.' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
