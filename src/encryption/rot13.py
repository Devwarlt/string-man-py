class Rot13(object):
    __FIRST_CHAR_UNICODE_LOWER: int = ord('a')
    __MIDDLE_CHAR_UNICODE_LOWER: int = ord('m')
    __LAST_CHAR_UNICODE_LOWER: int = ord('z')

    __FIRST_CHAR_UNICODE_UPPER: int = ord('A')
    __MIDDLE_CHAR_UNICODE_UPPER: int = ord('M')
    __LAST_CHAR_UNICODE_UPPER: int = ord('Z')

    __ROT13_SHIFT_VALUE: int = 13

    def __init__(self) -> None:
        pass

    @staticmethod
    def __shift_unicode(
        char_unicode: int,
        first_char_unicode: int,
        middle_char_unicode: int,
        last_char_unicode: int
    ) -> int:
        new_char_unicode: int = char_unicode
        if char_unicode >= first_char_unicode\
                and char_unicode <= last_char_unicode:
            if char_unicode > middle_char_unicode:
                new_char_unicode -= Rot13.__ROT13_SHIFT_VALUE
            else:
                new_char_unicode += Rot13.__ROT13_SHIFT_VALUE
            return new_char_unicode
        return None

    @staticmethod
    def encrypt(plain_text: str) -> str:
        '''
        Método para criptografia com a cifra de César ROT-13
        para qualquer texto de entrada.
        '''

        # Representa o texto criptografado com a cifra de César ROT-13.
        rot13_encrypted_text: str = ""

        # Realizar loop para todos os caracteres do texto de entrada.
        for char in plain_text:
            # Obter o código unicode do caracter de entrada.
            char_unicode: int = ord(char)

            # Verificação para range de codificação unicode para caracteres
            # a-z ou somente letras de padrão ReGex [a-z].
            new_char_unicode: int = Rot13.__shift_unicode(
                char_unicode,
                Rot13.__FIRST_CHAR_UNICODE_LOWER,
                Rot13.__MIDDLE_CHAR_UNICODE_LOWER,
                Rot13.__LAST_CHAR_UNICODE_LOWER
            )
            if new_char_unicode:
                # Incrementação do novo caracter criptografado.
                rot13_encrypted_text += chr(new_char_unicode)
                continue

            # Verificação para range de codificação unicode para caracteres
            # A-Z ou somente letras de padrão ReGex [A-Z].
            new_char_unicode: int = Rot13.__shift_unicode(
                char_unicode,
                Rot13.__FIRST_CHAR_UNICODE_UPPER,
                Rot13.__MIDDLE_CHAR_UNICODE_UPPER,
                Rot13.__LAST_CHAR_UNICODE_UPPER
            )
            if new_char_unicode:
                # Incrementação do novo caracter criptografado.
                rot13_encrypted_text += chr(new_char_unicode)
                continue

            # Inclusão de caracteres especiais ou numéricos.
            rot13_encrypted_text += char

        # Retorno do texto criptografado.
        return rot13_encrypted_text

    @staticmethod
    def decrypt(rot13_encrypted_text: str) -> str:
        return Rot13.encrypt(rot13_encrypted_text)
