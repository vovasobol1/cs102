import unittest
from vigenre import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_vigenere(self):
        # проверка шифрования
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("", "kluch"), "")

    def test_decrypt_vigenere(self):
        # Проверка дешифрования
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("", "KEY"), "")

    def test_type_check(self):
        # обработка исключений при невереном типе данных
        with self.assertRaises(TypeError):
            encrypt_vigenere(123, "KEY")
        with self.assertRaises(TypeError):
            decrypt_vigenere("CIPHER", 123)
        with self.assertRaises(TypeError):
            decrypt_vigenere([1 , 2 , 3 ], 'key')


if __name__ == "__main__":
    unittest.main()