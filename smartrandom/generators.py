# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Random Data Generators."""
import hashlib
import os
import re
import secrets
import string


class RandomLetterGenerator:
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase

    @classmethod
    def generate(cls, length: int) -> str:
        """
        Generates a random string of letters with at least one uppercase and one lowercase letter.

        :param length: Length of the generated string.
        :raises ValueError: If length is less than 2.
        :return: Random string of letters.
        """
        if length < 2:
            raise ValueError("The length must be at least 2 to include at "
                             "least one uppercase and one lowercase letter.")
        result = [
            secrets.choice(cls.upper_letters),
            secrets.choice(cls.lower_letters)
        ]
        result += [secrets.choice(cls.upper_letters + cls.lower_letters) for _ in range(length - 2)]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)


class RandomIntegerGenerator:
    digits = string.digits

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a string of random digits of the specified length.

        :param length: Length of the generated string.
        :raises ValueError: If length is less than 1.
        :return: Random string of digits.
        """
        if length < 1:
            raise ValueError("The length must be at least 1.")
        return ''.join(secrets.choice(cls.digits) for _ in range(length))


class RandomSymbolGenerator:
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a string of random symbols of the specified length.

        :param length: Length of the generated string.
        :raises ValueError: If length is less than 1.
        :return: Random string of symbols.
        """
        if length < 1:
            raise ValueError("The length must be at least 1.")
        return ''.join(secrets.choice(cls.symbols) for _ in range(length))


class HashGenerator:
    @classmethod
    def generate(cls, text: str) -> str:
        """
        Generates an SHA-3-512 hash for the given text.

        :param text: Input text to hash.
        :return: SHA-3-512 hash of the input text.
        """
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        return sha.hexdigest()


class UrandomGenerator:
    @classmethod
    def generate(cls, size: int = 128) -> bytes:
        """
        Generates random bytes of the specified size.

        :param size: Number of random bytes to generate.
        :return: Random bytes.
        """
        return os.urandom(size)

    @classmethod
    def generate_string(cls, size: int = 128) -> str:
        """
        Generates a random string in hexadecimal format of the specified size.

        :param size: Number of random bytes to generate.
        :return: Random string in hexadecimal format.
        """
        random_bytes = os.urandom(size)
        return random_bytes.hex()


class TextRandomizer:
    @classmethod
    def randomize(cls, text: str) -> str:
        """
        Randomizes the input text by replacing patterns enclosed in curly braces with randomly selected elements.

        The method looks for patterns in the input text that are enclosed in curly braces `{}`.
        Inside the braces, multiple options can be provided, separated by a vertical bar `|`.
        For each occurrence of such a pattern, one of the options is randomly selected and
        replaces the entire pattern in the text.

        For example:
        - Input: "Hello, {Alice|Bob|Charlie}!"
        - Output: "Hello, Bob!" (or "Hello, Alice!" or "Hello, Charlie!", randomly chosen)

        :param text: The input text containing patterns to be randomized.
        :return: The randomized text with patterns replaced by randomly selected options.
        """
        return re.sub(r"{(.+?)}", lambda x: secrets.choice(x.group(1).split("|")), text)


class SecretCodeGenerator:
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a random string containing uppercase letters, lowercase letters, and digits.

        :param length: Length of the generated string.
        :raises ValueError: If length is less than 3.
        :return: Random string of letters and digits.
        """
        if length < 3:
            raise ValueError("The length must be at least 3.")
        result = [
            secrets.choice(cls.upper_letters),
            secrets.choice(cls.lower_letters),
            secrets.choice(cls.digits),
        ]
        result += [
            secrets.choice(cls.upper_letters + cls.lower_letters + cls.digits) for _ in range(length - 3)
        ]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)


class PasswordGenerator:
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length: int = 10) -> str:
        """
        Generates a random password of the specified length, including uppercase letters,
        lowercase letters, digits, and symbols.

        :param length: Length of the generated password.
        :raises ValueError: If length is less than 4.
        :return: Random password.
        """
        if length < 4:
            raise ValueError("The length cannot be less than 4.")

        result = [
            secrets.choice(cls.upper_letters),
            secrets.choice(cls.lower_letters),
            secrets.choice(cls.digits),
            secrets.choice(cls.symbols),
        ]
        result += [
            secrets.choice(cls.upper_letters + cls.lower_letters + cls.digits + cls.symbols) for _ in range(length - 4)
        ]
        secrets.SystemRandom().shuffle(result)
        return ''.join(result)


class RandomDataGenerator:
    @staticmethod
    def generate_random_letters(length: int) -> str:
        """
        Generates a random string of letters.

        :param length: Length of the generated string.
        :return: Random string of letters.
        """
        return RandomLetterGenerator.generate(length)

    @staticmethod
    def generate_random_numbers(length: int) -> str:
        """
        Generates a random string of digits.

        :param length: Length of the generated string.
        :return: Random string of digits.
        """
        return RandomIntegerGenerator.generate(length)

    @staticmethod
    def generate_random_symbols(length: int) -> str:
        """
        Generates a random string of symbols.

        :param length: Length of the generated string.
        :return: Random string of symbols.
        """
        return RandomSymbolGenerator.generate(length)

    @staticmethod
    def generate_hash(text: str) -> str:
        """
        Generates a hash for the given text.

        :param text: Input text to hash.
        :return: Hash of the input text.
        """
        return HashGenerator.generate(text)

    @staticmethod
    def generate_random_bytes(size: int = 128) -> bytes:
        """
        Generates random bytes.

        :param size: Number of random bytes to generate.
        :return: Random bytes.
        """
        return UrandomGenerator.generate(size)

    @staticmethod
    def generate_random_hex_string(size: int = 128) -> str:
        """
        Generates a random string in hexadecimal format.

        :param size: Number of random bytes to generate.
        :return: Random string in hexadecimal format.
        """
        return UrandomGenerator.generate_string(size)

    @staticmethod
    def randomize_text(text: str) -> str:
        """
        Randomizes text by replacing patterns enclosed in curly braces.

        :param text: Input text with patterns.
        :return: Randomized text.
        """
        return TextRandomizer.randomize(text)

    @staticmethod
    def generate_password(length: int = 10) -> str:
        """
        Generates a random password.

        :param length: Length of the generated password.
        :return: Random password.
        """
        return PasswordGenerator.generate(length)

    @staticmethod
    def generate_secret_code(length: int = 6) -> str:
        """
        Generates a random string containing letters and digits.

        :param length: Length of the generated string.
        :return: Random string of letters and digits.
        """
        return SecretCodeGenerator.generate(length)
