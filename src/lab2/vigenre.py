def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # обратотка исклюючения
    if not isinstance(plaintext, str) or not isinstance(keyword, str):
        raise TypeError("параметры введены неверно")

    ciphertext = ""
    keyword = keyword.upper()  # Преобразуем ключ в верхний регистр
    keyword_len = len(keyword)  # Длина ключа

    for i in range(len(plaintext)):
        decrypted_char = ""
        char = plaintext[i]

        # если char это буква то выполним шифрование
        if char.isalpha():
            # определим сдвиг
            shift = ord(keyword[i % keyword_len]) - ord('A')

            if char.islower():
                # Расшифровать строчные буквы
                decrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Расшифровать заглавные буквы
                decrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # если символ не буква оставим его как есть
            decrypted_char += char

        ciphertext += decrypted_char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:

    # обратотка исклюючения
    if not isinstance(ciphertext, str) or not isinstance(keyword, str):
        raise TypeError("параметры введены неверно")

    plaintext = ""  # Переменная для хранения расшифрованного сообщения
    keyword = keyword.upper()  # Преобразуем ключ в верхний регистр
    keyword_len = len(keyword)  # Длина ключа

    for i, char in enumerate(ciphertext):  # Итерируемся по символам в зашифрованной строке
        if char.isalpha():
            # Если символ - буква, выполним дешифрование
            # Определяем сдвиг для текущей буквы на основе ключа
            shift = ord(keyword[i % keyword_len]) - ord('A')

            if char.islower():
                # Расшифровать строчные буквы
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                # Расшифровать заглавные буквы
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            # Если символ не является буквой, оставляем его как есть
            decrypted_char = char

        plaintext += decrypted_char  # Добавляем расшифрованный символ к расшифрованной строке

    return plaintext  # Возвращаем расшифрованное сообщение