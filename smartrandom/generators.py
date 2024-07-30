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
    def generate(cls, length):
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
    def generate(cls, length=10):
        if length < 1:
            raise ValueError("The length must be at least 1.")
        return ''.join(secrets.choice(cls.digits) for _ in range(length))


class RandomSymbolGenerator:
    symbols = '!@#$%&^_'

    @classmethod
    def generate(cls, length=10):
        if length < 1:
            raise ValueError("The length must be at least 1.")
        return ''.join((secrets.choice(cls.symbols) for _ in range(length)))


class HashGenerator:
    @classmethod
    def generate(cls, text: str):
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        new_hash = sha.hexdigest()
        return new_hash


class UrandomGenerator:
    @classmethod
    def generate(cls, size=128):
        random_bytes = os.urandom(size)
        return random_bytes

    @classmethod
    def generate_string(cls, size=128):
        random_bytes = os.urandom(size)
        return random_bytes.hex()


class TextRandomizer:

    @classmethod
    def randomize(cls, text):
        res = re.sub(r"{(.+?)}", lambda x: secrets.choice(x.group(1).split("|")), text)
        return res

    def __call__(self, message):
        return self.randomize(message)


class StringAndNumberCodeGenerator:
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits

    @classmethod
    def generate(cls, length=10):
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
    def generate(cls, length=10):
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


class RandomDataMaster:
    letters = RandomLetterGenerator()
    numbers = RandomIntegerGenerator()
    symbols = RandomSymbolGenerator()
    hash = HashGenerator()
    urandom = UrandomGenerator()
    text_randomizer = TextRandomizer()
    password = PasswordGenerator()
    string_and_numeric_code = StringAndNumberCodeGenerator()
