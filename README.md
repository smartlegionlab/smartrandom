# smartrandom

---

## Random Data Generators:

Allows you to generate random strings of a given length from letters, numbers, symbols.
Helps to generate passwords, service codes (for example, for sending via SMS), hashes and much more.
---

## Help:

```python
from smartrandom.random_master import RandomMaster

random_string = RandomMaster.string.get(length=10)
random_number_string = RandomMaster.number.get(length=10)
password = RandomMaster.password.get(length=10)
random_hash = RandomMaster.hash.get(text='give me hash')
random_number_code = RandomMaster.get_code(length=10, number_flag=True)
random_string_code = RandomMaster.get_code(length=10, string_flag=True)
random_symbol_code = RandomMaster.get_code(length=10, symbol_flag=True)

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
    Copyright © 2018-2023, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
