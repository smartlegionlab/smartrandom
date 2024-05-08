# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import hashlib
import random
import string


class RandomStringMaster:
    letters = string.ascii_letters

    @classmethod
    def create(cls, length=10):
        return ''.join((random.choice(cls.letters) for _ in range(length)))


class RandomNumberMaster:
    numbers = string.digits

    @classmethod
    def create(cls, length=10):
        return ''.join((random.choice(cls.numbers) for _ in range(length)))


class RandomSymbolMaster:
    symbols = '@$!%*#?&-'

    @classmethod
    def create(cls, length=10):
        return ''.join((random.choice(cls.symbols) for _ in range(length)))


class RandomPasswordMaster:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '@$!%*#?&-'

    @classmethod
    def create(cls, length=10):
        return ''.join((random.choice(cls.letters + cls.numbers + cls.symbols) for _ in range(length)))


class RandomHashMaster:
    @classmethod
    def create(cls, text):
        sha = hashlib.sha3_512(text.encode('utf-8'))
        new_hash = sha.hexdigest()
        return new_hash


class RandomMaster:
    string = RandomStringMaster()
    number = RandomNumberMaster()
    symbol = RandomSymbolMaster()
    password = RandomPasswordMaster()
    hash = RandomHashMaster()

    @classmethod
    def create_code(cls, length=10, number_flag=False, string_flag=False, symbol_flag=False):
        data = ''
        if string_flag:
            data += cls.string.letters
        if number_flag:
            data += cls.number.numbers
        if symbol_flag:
            data += cls.symbol.symbols
        return ''.join((random.choice(data) for _ in range(length)))
