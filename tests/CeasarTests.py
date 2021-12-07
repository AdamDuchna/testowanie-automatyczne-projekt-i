import unittest

from assertpy import assert_that

from src.Ceasar import Ceasar


class CeasarEncodeTest(unittest.TestCase):
    def setUp(self):
        assistant = Ceasar()
        self.temp = assistant.encode

    def test_Ceasar_encode_single_uppercase_letter(self):
        self.assertEqual('D', self.temp('A'))

    def test_Ceasar_encode_single_lowercase_letter(self):
        self.assertEqual('f', self.temp('c'))

    def test_Ceasar_encode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1')

    def test_Ceasar_encode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3)

    def test_Ceasar_encode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4])

    def test_Ceasar_encode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65)

    def test_Ceasar__object(self):
        self.assertRaises(TypeError, self.temp, {})

    def test_Ceasar_encode_tuple(self):
        self.assertRaises(TypeError, self.temp, ())

    def test_Ceasar_encode_boolean(self):
        self.assertRaises(TypeError, self.temp, True)

    def test_Ceasar_encode_word(self):
        self.assertEqual("nrw", self.temp("kot"))

    def test_Ceasar_encode_string_with_non_letters(self):
        self.assertRaises(ValueError, self.temp, "88krzyk!!!")

    def test_Ceasar_encode_empty_string(self):
        self.assertEqual("", self.temp(""))

    def test_Ceasar_encode_uppercase(self):
        self.assertEqual("YHQGHWWD", self.temp("VENDETTA"))

    def test_Ceasar_encode_letter_out_of_range(self):
        self.assertEqual("chwd", self.temp("zeta"))

    def test_Ceasar_encode_mixed_cases_and_out_of_range(self):
        self.assertEqual("CuBz VCCbENl", self.temp("ZrYw SZZyBKi"))

    def test_Ceasar_encode_whole_alphabet(self):
        self.assertEqual("def lmn gguvwxzabcghi jk opqrs", self.temp("abc ijk ddrstuwxyzdef gh lmnop"))

    def test_Ceasar_encode_whole_alphabet_uppercase(self):
        self.assertEqual("DEF LMN GGUVWXZABCGHI JK OPQRS", self.temp("ABC IJK DDRSTUWXYZDEF GH LMNOP"))

    def test_Ceasar_encode_special_signs_and_letters(self):
        self.assertRaises(ValueError, self.temp, "abc i "F" ?SD (###  jk ddrstuwxy !!! ! ! zdef gh lmnop")


def test_Ceasar_encoding_assertpy_is_string():
    assist = Ceasar()
    assert_that(assist.encode("ZAlEW wISLA")).is_type_of(str)


def test_Ceasar_encoding_assertpy_is_not_empty():
    assist = Ceasar()
    assert_that(assist.encode("LWS aaaa")).is_not_empty()


def test_Ceasar_encoding_assertpy_is_upper():
    assist = Ceasar()
    assert_that(assist.encode("CWKS")).is_upper()


def test_Ceasar_encoding_assertpy_is_lower():
    assist = Ceasar()
    assert_that(assist.encode("lolek")).is_lower()


def test_Ceasar_encoding_assertpy_equals_ignore_cases():
    assist = Ceasar()
    assert_that(assist.encode("Carthago delenda est")).is_equal_to_ignoring_case('fduwkdjr ghohqGd hvw')


class CeasarDecodeTest(unittest.TestCase):
    def setUp(self):
        assistant = Ceasar()
        self.temp = assistant.decode

    def test_Ceasar_decode_single_uppercase_letter(self):
        self.assertEqual('A', self.temp('D'))

    def test_Ceasar_decode_single_lowercase_letter(self):
        self.assertEqual('c', self.temp('f'))

    def test_Ceasar_decode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1')

    def test_Ceasar_decode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3)

    def test_Ceasar_decode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4])

    def test_Ceasar_decode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65)

    def test_Ceasar__object(self):
        self.assertRaises(TypeError, self.temp, {})

    def test_Ceasar_decode_tuple(self):
        self.assertRaises(TypeError, self.temp, ())

    def test_Ceasar_decode_boolean(self):
        self.assertRaises(TypeError, self.temp, True)

    def test_Ceasar_decode_word(self):
        self.assertEqual("kto", self.temp("nwr"))

    def test_Ceasar_decode_string_with_non_letters(self):
        self.assertRaises(ValueError, self.temp, "88krzyk!!!")

    def test_Ceasar_decode_empty_string(self):
        self.assertEqual("", self.temp(""))

    def test_Ceasar_decode_uppercase(self):
        self.assertEqual("VENDETTA", self.temp("YHQGHWWD"))

    def test_Ceasar_decode_letter_out_of_range(self):
        self.assertEqual("zeta", self.temp("chwd"))

    def test_Ceasar_decode_mixed_cases_and_out_of_range(self):
        self.assertEqual("ZrYw SZZyBKi", self.temp("CuBz VCCbENl"))

    def test_Ceasar_decode_whole_alphabet(self):
        self.assertEqual("abc ijk ddrstuwxyzdef gh lmnop", self.temp("def lmn gguvwxzabcghi jk opqrs"))

    def test_Ceasar_decode_whole_alphabet_uppercase(self):
        self.assertEqual("ABC IJK DDRSTUWXYZDEF GH LMNOP", self.temp("DEF LMN GGUVWXZABCGHI JK OPQRS"))

    def test_Ceasar_decode_special_signs_and_letters(self):
        self.assertRaises(ValueError, self.temp, "abc i "F" ?SD (###  jk ddrstuwxy !!! ! ! zdef gh lmnop")


if __name__ == "__main__":
    unittest.main()
