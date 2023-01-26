import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):        
    def test_english_to_french_equal(self):      
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english_equal(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french_IsNull(self):
        self.assertIsNone(english_to_french(None), "The value is null")

    def test_french_to_english_IsNull(self):
        self.assertIsNone(french_to_english(None), "The value is null")

if __name__ == '__main__':
    unittest.main()