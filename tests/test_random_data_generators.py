# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import hashlib
import re

import pytest
import string
from smartrandom import RandomLetterGenerator, RandomIntegerGenerator, RandomSymbolGenerator, HashGenerator, \
    UrandomGenerator, TextRandomizer, SecretCodeGenerator, BasePasswordGenerator, PasswordGenerator, \
    SmartPasswordGenerator, RandomDataGenerator


class TestRandomLetterGenerator:

    def test_generate_length(self):
        length = 10
        result = RandomLetterGenerator.generate(length)
        assert len(result) == length

    def test_generate_min_length(self):
        with pytest.raises(ValueError, match="The length must be at least 2"):
            RandomLetterGenerator.generate(1)

    def test_generate_contains_upper_and_lower(self):
        length = 10
        result = RandomLetterGenerator.generate(length)
        assert any(c in string.ascii_uppercase for c in result)
        assert any(c in string.ascii_lowercase for c in result)

    def test_generate_multiple_times(self):
        length = 10
        results = {RandomLetterGenerator.generate(length) for _ in range(100)}
        assert len(results) > 1


class TestRandomIntegerGenerator:

    def test_generate_length(self):
        length = 10
        result = RandomIntegerGenerator.generate(length)
        assert len(result) == length

    def test_generate_min_length(self):
        with pytest.raises(ValueError, match="The length must be at least 1."):
            RandomIntegerGenerator.generate(0)

    def test_generate_contains_only_digits(self):
        length = 10
        result = RandomIntegerGenerator.generate(length)
        assert all(c in string.digits for c in result)

    def test_generate_multiple_times(self):
        length = 10
        results = {RandomIntegerGenerator.generate(length) for _ in range(100)}
        assert len(results) > 1


class TestRandomSymbolGenerator:

    def test_generate_length(self):
        length = 10
        result = RandomSymbolGenerator.generate(length)
        assert len(result) == length

    def test_generate_min_length(self):
        with pytest.raises(ValueError, match="The length must be at least 1."):
            RandomSymbolGenerator.generate(0)

    def test_generate_contains_only_symbols(self):
        length = 10
        result = RandomSymbolGenerator.generate(length)
        assert all(c in RandomSymbolGenerator.symbols for c in result)

    def test_generate_multiple_times(self):
        length = 10
        results = {RandomSymbolGenerator.generate(length) for _ in range(100)}
        assert len(results) > 1


class TestHashGenerator:

    def test_generate_hash(self):
        text = "Hello, World!"
        expected_hash = hashlib.sha3_512(text.encode('utf-8')).hexdigest()
        result = HashGenerator.generate(text)
        assert result == expected_hash

    def test_generate_same_hash_for_same_input(self):
        text = "Test String"
        hash1 = HashGenerator.generate(text)
        hash2 = HashGenerator.generate(text)
        assert hash1 == hash2

    def test_generate_different_hashes_for_different_inputs(self):
        text1 = "First String"
        text2 = "Second String"
        hash1 = HashGenerator.generate(text1)
        hash2 = HashGenerator.generate(text2)
        assert hash1 != hash2


class TestUrandomGenerator:

    def test_generate_bytes_size(self):
        size = 128
        result = UrandomGenerator.generate(size)
        assert len(result) == size
        assert isinstance(result, bytes)

    def test_generate_string_size(self):
        size = 128
        result = UrandomGenerator.generate_string(size)
        assert len(result) == size * 2
        assert isinstance(result, str)

    def test_generate_bytes_randomness(self):
        size = 128
        results = {UrandomGenerator.generate(size) for _ in range(100)}
        assert len(results) > 1

    def test_generate_string_randomness(self):
        size = 128
        results = {UrandomGenerator.generate_string(size) for _ in range(100)}
        assert len(results) > 1


class TestTextRandomizer:

    def test_randomize_with_patterns(self):
        text = "Hello, {Alice|Bob|Charlie}!"
        result = TextRandomizer.randomize(text)
        assert re.match(r"Hello, (Alice|Bob|Charlie)!", result)

    def test_randomize_without_patterns(self):
        text = "Hello, World!"
        result = TextRandomizer.randomize(text)
        assert result == text

    def test_randomize_multiple_patterns(self):
        text = "{Good|Bad} morning, {Alice|Bob|Charlie}!"
        results = [TextRandomizer.randomize(text) for _ in range(100)]
        assert any(re.match(r"(Good|Bad) morning, (Alice|Bob|Charlie)!", result) for result in results)

    def test_randomize_consistency(self):
        text = "Hello, {Alice|Bob|Charlie}!"
        results = {TextRandomizer.randomize(text) for _ in range(100)}
        assert len(results) > 1


class TestSecretCodeGenerator:

    def test_generate_default_length(self):
        code = SecretCodeGenerator.generate()
        assert len(code) == 10
        assert any(c in string.ascii_uppercase for c in code)
        assert any(c in string.ascii_lowercase for c in code)
        assert any(c in string.digits for c in code)

    def test_generate_custom_length(self):
        length = 15
        code = SecretCodeGenerator.generate(length)
        assert len(code) == length
        assert any(c in string.ascii_uppercase for c in code)
        assert any(c in string.ascii_lowercase for c in code)
        assert any(c in string.digits for c in code)

    def test_generate_length_too_short(self):
        with pytest.raises(ValueError, match="The length must be at least 3."):
            SecretCodeGenerator.generate(2)

    def test_generate_length_edge_case(self):
        code = SecretCodeGenerator.generate(3)
        assert len(code) == 3
        assert any(c in string.ascii_uppercase for c in code)
        assert any(c in string.ascii_lowercase for c in code)
        assert any(c in string.digits for c in code)

    def test_generate_unique_codes(self):
        codes = {SecretCodeGenerator.generate() for _ in range(1000)}
        assert len(codes) > 900


class TestBasePasswordGenerator:

    def test_generate_default_length(self):
        password = BasePasswordGenerator.generate()
        assert len(password) == 10

    def test_generate_custom_length(self):
        length = 15
        password = BasePasswordGenerator.generate(length)
        assert len(password) == length

    def test_generate_length_too_short(self):
        with pytest.raises(ValueError, match="The length must be at least 3."):
            BasePasswordGenerator.generate(3)

    def test_generate_unique_passwords(self):
        num_passwords = 1000
        passwords = {BasePasswordGenerator.generate(10) for _ in range(num_passwords)}
        assert len(passwords) == num_passwords


class TestPasswordGenerator:

    def test_generate_default_length(self):
        password = PasswordGenerator.generate()
        assert len(password) == 10
        assert any(c in string.ascii_uppercase for c in password)
        assert any(c in string.ascii_lowercase for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in '!@#$%&^_' for c in password)

    def test_generate_custom_length(self):
        length = 15
        password = PasswordGenerator.generate(length)
        assert len(password) == length
        assert any(c in string.ascii_uppercase for c in password)
        assert any(c in string.ascii_lowercase for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in '!@#$%&^_' for c in password)

    def test_generate_length_too_short(self):
        with pytest.raises(ValueError, match="The length cannot be less than 4."):
            PasswordGenerator.generate(3)

    def test_generate_length_edge_case(self):
        password = PasswordGenerator.generate(4)
        assert len(password) == 4
        assert any(c in string.ascii_uppercase for c in password)
        assert any(c in string.ascii_lowercase for c in password)
        assert any(c in string.digits for c in password)
        assert any(c in '!@#$%&^_' for c in password)

    def test_generate_unique_passwords(self):
        num_passwords = 1000
        passwords = {PasswordGenerator.generate(10) for _ in range(num_passwords)}
        assert len(passwords) > 900


class TestSmartPasswordGenerator:

    def test_generate_with_custom_seed(self):
        seed = "custom_seed"
        password = SmartPasswordGenerator.generate(seed=seed, length=15)
        assert len(password) == 15
        assert isinstance(password, str)

    def test_generate_without_seed(self):
        password = SmartPasswordGenerator.generate(length=15)
        assert len(password) == 15
        assert isinstance(password, str)

    def test_generate_with_different_seeds(self):
        seed1 = "seed1"
        seed2 = "seed2"
        password1 = SmartPasswordGenerator.generate(seed=seed1, length=15)
        password2 = SmartPasswordGenerator.generate(seed=seed2, length=15)
        assert password1 != password2

    def test_generate_with_same_seed(self):
        seed = "same_seed"
        password1 = SmartPasswordGenerator.generate(seed=seed, length=15)
        password2 = SmartPasswordGenerator.generate(seed=seed, length=15)
        assert password1 == password2

    def test_generate_with_empty_seed(self):
        password = SmartPasswordGenerator.generate(seed='', length=15)
        assert len(password) == 15
        assert isinstance(password, str)

    def test_generate_length_too_short(self):
        with pytest.raises(ValueError, match="The length cannot be less than 4."):
            SmartPasswordGenerator.generate(seed="test", length=3)


class TestRandomDataGenerator:

    def test_generate_random_letters(self):
        length = 10
        result = RandomDataGenerator.generate_random_letters(length)
        assert len(result) == length
        assert all(c in string.ascii_letters for c in result)

    def test_generate_random_numbers(self):
        length = 10
        result = RandomDataGenerator.generate_random_numbers(length)
        assert len(result) == length
        assert all(c in string.digits for c in result)

    def test_generate_random_symbols(self):
        length = 10
        result = RandomDataGenerator.generate_random_symbols(length)
        assert len(result) == length
        assert all(c in '!@#$%&^_' for c in result)

    def test_generate_hash(self):
        text = "test"
        result = RandomDataGenerator.generate_hash(text)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_generate_random_bytes(self):
        size = 128
        result = RandomDataGenerator.generate_random_bytes(size)
        assert len(result) == size

    def test_generate_random_hex_string(self):
        size = 128
        result = RandomDataGenerator.generate_random_hex_string(size)
        assert len(result) == size * 2
        assert all(c in string.hexdigits for c in result)

    def test_randomize_text(self):
        text = "Hello {name}!"
        result = RandomDataGenerator.randomize_text(text)
        assert isinstance(result, str)
        assert "Hello " in result

    def test_generate_base_password(self):
        length = 10
        password = RandomDataGenerator.generate_base_password(length)
        assert len(password) == length

    def test_generate_smart_password(self):
        seed = "test_seed"
        length = 15
        password = RandomDataGenerator.generate_smart_password(seed, length)
        assert len(password) == length

    def test_generate_password(self):
        length = 10
        password = RandomDataGenerator.generate_password(length)
        assert len(password) == length

    def test_generate_secret_code(self):
        length = 6
        code = RandomDataGenerator.generate_secret_code(length)
        assert len(code) == length
        assert all(c in string.ascii_letters + string.digits for c in code)
