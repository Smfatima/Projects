import unittest
from first_project import has_vowel, check_sentence  # Replace 'your_code_file' with the actual filename containing your code

class TestHasVowel(unittest.TestCase):
    def test_has_vowel(self):
        self.assertTrue(has_vowel("hello"))
        self.assertTrue(has_vowel("world"))
        self.assertFalse(has_vowel("fly"))
        self.assertFalse(has_vowel("sky"))

class TestCheckSentence(unittest.TestCase):
    def test_check_sentence(self):
        self.assertEqual(check_sentence("This is a test"), "Write again")
        self.assertEqual(check_sentence("Fly high in the sky"), "Stop")
        self.assertEqual(check_sentence("No vowels here"), "Write again")

if __name__ == '__main__':
    unittest.main()