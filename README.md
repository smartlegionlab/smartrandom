# smartrandom <sup>v0.1.2</sup>
---

## Random Data Generators:

>Allows you to generate random strings of a given length from letters, numbers, and symbols.
>Helps to generate passwords, service codes (for example, for sending via SMS), hashes, and much more.

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
