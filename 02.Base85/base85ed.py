"""
Base85 encoder and decoder
"""

from __future__ import annotations
from beartype import beartype

_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
_DECODE_MAP = {ord(c): i for i, c in enumerate(_ALPHABET)}


@beartype
def encode(b: bytes) -> bytes:
    if not b:
        return b""

    result = []

    for i in range(0, len(b), 4):
        chunk = b[i:i + 4]
        ours_len = len(chunk)

        # Выравнивание до 4 байт нулями
        padded = chunk + b'\x00' * (4 - ours_len)
        num = int.from_bytes(padded, 'big')

        # Извлекаем 5 цифр base85 (младшие первыми)
        digits = []
        for _ in range(5):
            digits.append(num % 85)
            num //= 85
        digits.reverse()

        # Количество символов для вывода: ours_len + 1
        chars_to_keep = ours_len + 1
        for d in digits[:chars_to_keep]:
            result.append(_ALPHABET[d])

    return ''.join(result).encode('ascii')


@beartype
def decode(b: bytes) -> bytes:
    if not b:
        return b""

    text = b.decode('ascii')
    result = bytearray()

    for i in range(0, len(text), 5):
        chunk = text[i:i + 5]
        chunk_len = len(chunk)

        # Дополняем до 5 символов максимальным значением ('~')
        padded_chunk = chunk + '~' * (5 - chunk_len)

        num = 0
        for char in padded_chunk:
            num = num * 85 + _DECODE_MAP[ord(char)]

        decoded_bytes = num.to_bytes(4, 'big')

        # Определяем сколько реальных байт было закодировано
        if chunk_len == 1:
            take = 1
        else:
            take = chunk_len - 1

        result.extend(decoded_bytes[:take])

    return bytes(result)


