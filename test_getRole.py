import unittest
from role import getRole


class TestGetRole(unittest.TestCase):

    def test_single_word_single_noun(self):
        self.assertEqual(getRole(role='user'), ['user'])

    def test_single_word_no_noun_1(self):
        with self.assertRaises(Exception) as context:
            getRole(role='walking')

        self.assertTrue('You must have a single role' in str(context.exception))

    def test_single_word_no_noun_2(self):
        with self.assertRaises(Exception) as context:
            getRole(role='Jack')

        self.assertTrue('You must have a single role' in str(context.exception))

    def test_multiple_words_no_noun(self):
        with self.assertRaises(Exception) as context:
            getRole(role='Jack walks and pees')

        self.assertTrue('You must have a single role' in str(context.exception))

    def test_multiple_words_single_noun_1(self):
        self.assertEqual(getRole(role='dog walker'), ['dog walker'])

    def test_multiple_words_single_noun_2(self):
        self.assertEqual(getRole(role='dog bed manufacturer'), ['dog bed manufacturer'])

    def test_multiple_words_multiple_nouns_1(self):
        with self.assertRaises(Exception) as context:
            getRole(role='parking valet and owner')

        self.assertTrue('You must have a single role' in str(context.exception))

    def test_multiple_words_multiple_nouns_2(self):
        with self.assertRaises(Exception) as context:
            getRole(role='user and developer')

        self.assertTrue('You must have a single role' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
