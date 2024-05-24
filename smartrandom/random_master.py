# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
"""Random Data Generators."""
import hashlib
import os
import random
import string


class RandomLettersMaster:
    letters = string.ascii_letters

    @classmethod
    def create(cls, length=10):
        return ''.join((random.choice(cls.letters) for _ in range(length)))


class RandomNumericMaster:
    numbers = string.digits

    @classmethod
    def create(cls, length=10):
        return ''.join((random.choice(cls.numbers) for _ in range(length)))


class RandomSymbolsMaster:
    symbols = '!@#$%&^_'

    @classmethod
    def create(cls, length=10):
        return ''.join((random.choice(cls.symbols) for _ in range(length)))


class HashMaster:
    @classmethod
    def create(cls, text: str):
        text = str(text)
        sha = hashlib.sha3_512(text.encode('utf-8'))
        new_hash = sha.hexdigest()
        return new_hash


class UrandomGen:
    @classmethod
    def generate(cls, size=32):
        return os.urandom(size)


class RandomStringMaster:
    letters_master = RandomLettersMaster()
    numeric_master = RandomNumericMaster()
    symbols_master = RandomSymbolsMaster()
    hash_master = HashMaster()
    urandom_gen = UrandomGen()

    @classmethod
    def create_string(cls, length=10):
        random_string = cls.letters_master.letters + cls.numeric_master.numbers + cls.symbols_master.symbols
        return ''.join((random.choice(random_string) for _ in range(length)))

    @classmethod
    def create_hash(cls, text):
        return cls.hash_master.create(text)

    @classmethod
    def create_numeric_code(cls, length):
        return cls.numeric_master.create(length)

    @classmethod
    def create_letters_code(cls, length):
        return cls.letters_master.create(length)

    @classmethod
    def create_symbols_code(cls, length):
        return cls.symbols_master.create(length)

    @classmethod
    def create_code(cls, length=10, numeric_flag=False, letters_flag=False, symbols_flag=False):
        data = ''
        if letters_flag:
            data += cls.letters_master.letters
        if numeric_flag:
            data += cls.numeric_master.numbers
        if symbols_flag:
            data += cls.symbols_master.symbols
        if data:
            return ''.join((random.choice(data) for _ in range(length)))
        return None

    @classmethod
    def get_random_bytes(cls, size):
        return cls.urandom_gen.generate(size)
