# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import pytest
from smartrandom import (
    RandomLetterGenerator,
    RandomIntegerGenerator,
    RandomSymbolGenerator,
    HashGenerator,
    UrandomGenerator,
    TextRandomizer,
    SecretCodeGenerator,
    PasswordGenerator,
    RandomDataGenerator
)


def test_random_letter_generator():
    # Test valid length
    result = RandomLetterGenerator.generate(10)
    assert len(result) == 10
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)

    # Test invalid length
    with pytest.raises(ValueError):
        RandomLetterGenerator.generate(1)


def test_random_integer_generator():
    # Test valid length
    result = RandomIntegerGenerator.generate(5)
    assert len(result) == 5
    assert result.isdigit()

    # Test invalid length
    with pytest.raises(ValueError):
        RandomIntegerGenerator.generate(0)


def test_random_symbol_generator():
    # Test valid length
    result = RandomSymbolGenerator.generate(5)
    assert len(result) == 5
    assert all(c in RandomSymbolGenerator.symbols for c in result)

    # Test invalid length
    with pytest.raises(ValueError):
        RandomSymbolGenerator.generate(0)


def test_hash_generator():
    text = "test"
    result = HashGenerator.generate(text)
    assert isinstance(result, str)
    assert len(result) == 128  # SHA-3-512 produces a 128-character hex string


def test_urandom_generator():
    # Test random bytes generation
    result = UrandomGenerator.generate(16)
    assert len(result) == 16
    assert isinstance(result, bytes)

    # Test random hex string generation
    hex_result = UrandomGenerator.generate_string(16)
    assert len(hex_result) == 32  # 16 bytes = 32 hex characters


def test_text_randomizer():
    text = "Hello {world|everyone}"
    result = TextRandomizer.randomize(text)
    assert result in ["Hello world", "Hello everyone"]


def test_secret_code_generator():
    # Test valid length
    result = SecretCodeGenerator.generate(10)
    assert len(result) == 10
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)
    assert any(c.isdigit() for c in result)

    # Test invalid length
    with pytest.raises(ValueError):
        SecretCodeGenerator.generate(2)


def test_password_generator():
    # Test valid length
    result = PasswordGenerator.generate(12)
    assert len(result) == 12
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)
    assert any(c.isdigit() for c in result)
    assert any(c in PasswordGenerator.symbols for c in result)

    # Test invalid length
    with pytest.raises(ValueError):
        PasswordGenerator.generate(3)


def test_random_data_generator():
    # Test random letters
    letters = RandomDataGenerator.generate_random_letters(10)
    assert len(letters) == 10

    # Test random numbers
    numbers = RandomDataGenerator.generate_random_numbers(5)
    assert len(numbers) == 5
    assert numbers.isdigit()

    # Test random symbols
    symbols = RandomDataGenerator.generate_random_symbols(5)
    assert len(symbols) == 5
    assert all(c in RandomSymbolGenerator.symbols for c in symbols)

    # Test hash generation
    hash_result = RandomDataGenerator.generate_hash("test")
    assert isinstance(hash_result, str)
    assert len(hash_result) == 128

    # Test random bytes
    random_bytes = RandomDataGenerator.generate_random_bytes(16)
    assert len(random_bytes) == 16
    assert isinstance(random_bytes, bytes)

    # Test random hex string
    hex_string = RandomDataGenerator.generate_random_hex_string(16)
    assert len(hex_string) == 32

    # Test text randomization
    randomized_text = RandomDataGenerator.randomize_text("Hello {world|everyone}")
    assert randomized_text in ["Hello world", "Hello everyone"]

    # Test password generation
    password = RandomDataGenerator.generate_password(12)
    assert len(password) == 12
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in PasswordGenerator.symbols for c in password)

    # Test secret code generation
    secret_code = RandomDataGenerator.generate_secret_code(10)
    assert len(secret_code) == 10
    assert any(c.isupper() for c in secret_code)
    assert any(c.islower() for c in secret_code)
    assert any(c.isdigit() for c in secret_code)


if __name__ == "__main__":
    pytest.main()
