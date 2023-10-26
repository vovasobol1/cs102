def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE

    # проверка на то , что поступили правильные параметры
    if not isinstance(plaintext, str) or not isinstance(shift, int):
        raise ValueError("параметры введены неверно")

    # пройдемся по каждому символу в строке
    for char in plaintext:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Определяем регистр символа (верхний или нижний)
            is_upper = char.isupper()
            # Преобразуем символ в верхний регистр для унификации
            char = char.upper()
            # Вычисляем сдвиг, учитывая алфавит с 26 буквами
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            # Если исходный символ был в верхнем регистре, сохраняем его в верхнем регистре
            if is_upper:
                shifted_char = shifted_char.upper()
            else:
                shifted_char = shifted_char.lower()
            # Добавляем зашифрованный символ к результату
            ciphertext += shifted_char
        else:
            # Если символ не является буквой, оставляем его без изменений
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE

    # проверка на то , что поступили правильные параметры
    if not isinstance(plaintext, str) or not isinstance(shift, int):
        raise ValueError("параметры введены неверно")

    # Пройдемся по каждому символу в зашифрованном тексте
    for char in ciphertext:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Определяем регистр символа (верхний или нижний)
            is_upper = char.isupper()
            # Преобразуем символ в верхний регистр для унификации
            char = char.upper()
            # Вычисляем сдвиг назад в алфавите
            shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            # Если исходный символ был в верхнем регистре, сохраняем его в верхнем регистре
            if is_upper:
                shifted_char = shifted_char.upper()
            else:
                shifted_char = shifted_char.lower()
            # Добавляем расшифрованный символ к результату
            plaintext += shifted_char
        else:
            # Если символ не является буквой, оставляем его без изменений
            plaintext += char
    return plaintext
