# str2bool3 v1.0.0

## About
Convert string to boolean.  
The library recognizes "yes", "true", "y", "t", "1" as True, and "no", "false", "n", "f", "0" as False.  
Case insensitive.

## Installation

    $ pip install str2bool3

## Examples
Here's a basic example:

    >>> from str2bool3 import StrUtils
    >>> print(StrUtils.str2bool('Yes'))
    True

To raise an exception on invalid input:

    >>> from str2bool3 import StrUtils
    >>> StrUtils.str2bool_exc('invalid')
    ValueError: Invalid value 'invalid'. Expected one of: false, f, n, no, t, true, y, yes, 0, 1.

## License
BSD

Forked from symonsoft/str2bool
