from numtoword.numtoword import num_to_word
import unittest


class TestNumToWord(unittest.TestCase):
    def test_one(self):
        assert "one" == num_to_word(1)

    def test_two(self):
        assert "two" == num_to_word(2)

    def test_ten(self):
        assert "ten" == num_to_word(10)

    def test_eleven(self):
        assert "eleven" == num_to_word(11)

    def test_nineteen(self):
        assert "nineteen" == num_to_word(19)

    def test_twenty(self):
        assert "twenty" == num_to_word(20)

    def test_twenty_one(self):
        assert "twentyone" == num_to_word(21)

    def test_twenty_two(self):
        assert "twentytwo" == num_to_word(22)

    def test_thirty(self):
        assert "thirty" == num_to_word(30)

    def test_fifty_three(self):
        assert "fiftythree" == num_to_word(53)

    def test_one_hundred(self):
        assert "onehundred" == num_to_word(100)

    def test_three_hundred(self):
        assert "threehundred" == num_to_word(300)

    def test_one_hundred_twenty_three(self):
        assert "onehundredtwentythree" == num_to_word(123)

    def test_one_thousand(self):
        assert "onethousand" == num_to_word(1000)

    def test_one_thousand_two_hundred_thirty_two(self):
        assert "onethousandtwohundredthirtytwo" == num_to_word(1232)
