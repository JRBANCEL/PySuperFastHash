PySuperFastHash
===============

## SuperFastHash Python Implementation

### What is SuperFastHash ?
**SuperFastHash** is a non cryptographic hash function designed by **Paul Hsieh** : http://www.azillionmonkeys.com/qed/hash.html.

### Why implementing it in Python ?
A hash function is usually intensively used, so a fast implementation is needed. That is why previous Python SuperFastHash implementation are implemented using C or C++ and CPython interface.
For a project where this hash function is used only a few times and where speed is not critical, I implemented it in pure Python to remove dependencies and mainly for fun. So obviouly, It is slow.