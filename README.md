# smartrandom <sup>v0.2.1</sup>
---

## Random Data Generators:

Random data generators. Allows you to generate random strings of a given length from letters, numbers and symbols, as well as randomize text. Helps generate passwords, service codes (for example, for sending via SMS), hashes and much more. Generates smart, recoverable passwords.

---

[![PyPI Downloads](https://static.pepy.tech/badge/smartrandom)](https://pepy.tech/projects/smartrandom)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartrandom)](https://github.com/smartlegionlab/smartrandom/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartrandom?label=pypi%20downloads)](https://pypi.org/project/smartrandom/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartrandom)
[![PyPI](https://img.shields.io/pypi/v/smartrandom)](https://pypi.org/project/smartrandom)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartrandom)](https://github.com/smartlegionlab/smartrandom/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartrandom)](https://pypi.org/project/smartrandom)

***

Author and developer: ___A.A. Suvorov.___

***

## What is news:

smartrandom 0.2.1 - new improved version of the library.

- Added a regular password generator.
- Added a smart password generator.
- Improved tests

***

## Help:

`pip install smartrandom`

```python
from smartrandom import RandomDataGenerator


secret_code = RandomDataGenerator.generate_secret_code(length=6) # 'zREkjF'
number_secret_code = RandomDataGenerator.generate_random_numbers(length=6) # '986741'
symbols = RandomDataGenerator.generate_random_symbols(length=10) # '&&!@@&@!_!'
hash_ = RandomDataGenerator.generate_hash(text='text') # '1798b0ae66b1ca6f3b88e00f9d17ce1470549e97687a1c97e26110bb8853ad41797e83831efe7eedbd29042a9a8991fd1adb4f7680946d57eed99b8b6e5502c4'
urandom_string = RandomDataGenerator.generate_random_hex_string(size=32) # '7b1dd304b42e79d9e26bfb9f839abf8d001fed2039bcc3c5bfd14c0b05cfcab2'
urandom_bytes = RandomDataGenerator.generate_random_bytes(size=32) # b'f_@\x1bnP\xb4\xa8\xb7$a\xbf\x13\r#\x96\xe5\x07D\xa1N\xf5\xe9\x9a\x95\x91\xe4\xd0\x8fR"\''
randomized_text = RandomDataGenerator.randomize_text('{Salute|Hello|Good morning} {comrade|buddy|dear friend}!') # Good morning buddy!
password = RandomDataGenerator.generate_password(length=15) # 'b$L^#7rfIUzgY!2'
base_password = RandomDataGenerator.generate_base_password(length=15) # '$yE$JL8heeJQv5X'
smart_password1 = RandomDataGenerator.generate_smart_password(seed='test', length=15) # 'GEyfYrC%VJU!RSY'
smart_password2 = RandomDataGenerator.generate_smart_password(seed='test2', length=15) # '2PhIQt8pIke9c@m'
smart_password3 = RandomDataGenerator.generate_smart_password(seed='test', length=15) # 'GEyfYrC%VJU!RSY'
smart_password4 = RandomDataGenerator.generate_smart_password(seed='test2', length=15) # '2PhIQt8pIke9c@m'

```

### Text randomizer:

"Text randomization" or "variable text". It is used to create different variations of the same message.

You are using special syntax. Example: `'{Salute|Hello|Good morning} {comrade|buddy|dear friend}!'`

This syntax allows you to create variable messages by using curly braces and vertical bars to indicate alternatives.

Basic elements of syntax:

1. Curly braces {}: Used to group text options. Anything inside the curly braces will be randomly selected when generating the text.
2. Vertical bar |: Used to separate different text options within curly braces. Each option will be treated as a separate choice.

Example of use:

- Syntax: `'{Salute|Hello|Good morning} {comrade|buddy|dear friend}!'`
- Possible results:
    - Salute comrade!
    - Salute buddy!
    - Salute dear friend!
    - Hello comrade!
    - Hello buddy!
    - Hello dear friend!
    - Good morning comrade!
    - Good morning buddy!
    - Good morning dear friend!
- How to use:
  1. Create your text: Identify which parts of your message can vary and place them in curly braces.
  2. Add options: Separate alternatives with a vertical bar.
  3. Text Generation: Use RandomStringMaster() to generate a random message.

- Notes:
    - Make sure all options inside the curly braces make sense and fit the context.
    - You can use multiple randomization groups in a single message to create more complex variations.


Example of text randomization:

```python
from smartrandom import TextRandomizer

text = '{Salute|Hello|Good morning} {comrade|buddy|dear friend}!'
randomized_text = TextRandomizer.randomize(text)
print(randomized_text)  # Good morning buddy!
```

---

### Test coverage:

#### Run tests:
- `pip install pytest`
- `pytest -v`
  

#### __Test coverage 100%__

- `pip install pytest-coverage`
- `pytest --cov`

![commandpack image](https://github.com/smartlegionlab/smartrandom/raw/master/data/images/coverage_report.png)


#### Report html:

- `pytest --cov --cov-report=html`

***


***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
