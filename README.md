# smartrandom <sup>v0.1.3</sup>
---

## Random Data Generators:

Allows you to generate random strings of a given length from letters, numbers and symbols, as well as randomize text.
Helps generate passwords, service codes (for example, for sending via SMS), hashes and much more.

---

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

- Added the ability to randomize text.

***

## Help:

`pip install smartrandom`

```python
from smartrandom.random_master import RandomStringMaster

random_string = RandomStringMaster.create_string(length=10)
string_hash = RandomStringMaster.create_hash('text')
number_code = RandomStringMaster.create_numeric_code(length=6)
letter_code = RandomStringMaster.create_letters_code(length=6)
symbol_code = RandomStringMaster.create_letters_code(length=6)
code = RandomStringMaster.create_code(length=10, numeric_flag=True, letters_flag=True, symbols_flag=True)

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
from smartrandom.random_master import RandomStringMaster

random_master = RandomStringMaster()

text = '{Salute|Hello|Good morning} {comrade|buddy|dear friend}!'
randomized_text = random_master.randomize_text(text)
print(randomized_text) # Good morning buddy!
```

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
