import unittest

from .. import generator


class TestClass(unittest.TestCase):
    def setUp(self):
        self.inp = ('foo', 'bar', 'foobar')

    def test_sample_single_word(self):
        word = generator.sample(self.inp)
        assert word in self.inp

    def test_sample_multiple_words(self):
        words = generator.sample(self.inp, 2)
        assert len(words) == 2
        assert words[0] in self.inp
        assert words[1] in self.inp
        assert words[0] is not words[1]

    def test_generate_buzz_of_at_least_five_words(self):
        phrase = generator.generate_buzz()
        assert len(phrase.split()) >= 5
