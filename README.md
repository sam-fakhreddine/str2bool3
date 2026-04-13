# str2bool3 v1.4.0

## About
Convert a string (or compatible type) to a boolean value.

Recognized **True** values: `yes`, `true`, `t`, `y`, `1`  
Recognized **False** values: `no`, `false`, `f`, `n`, `0`  

Matching is case-insensitive and leading/trailing whitespace is stripped automatically.

`bool` and `int` inputs are also accepted directly:
- `True` / `False` → returned as-is  
- `1` → `True`, `0` → `False`

## Installation

    $ pip install str2bool3

## Examples

Basic usage:

    >>> from str2bool3 import str2bool
    >>> str2bool('Yes')
    True
    >>> str2bool('no')
    False
    >>> str2bool('  TRUE  ')   # whitespace stripped
    True
    >>> str2bool(True)          # bool pass-through
    True
    >>> str2bool(1)             # int support
    True

Unrecognized values return `None` by default (or a custom default):

    >>> str2bool('maybe')
    None
    >>> str2bool('maybe', default=False)
    False

Raise an exception for invalid input:

    >>> str2bool('maybe', raise_exc=True)
    ValueError: Invalid value 'maybe'. Expected one of: 0, 1, f, false, n, no, t, true, y, yes.

Convenience wrapper that always raises on invalid input (including `None`):

    >>> from str2bool3 import str2bool_exc
    >>> str2bool_exc('invalid')
    ValueError: Invalid value 'invalid'. Expected one of: 0, 1, f, false, n, no, t, true, y, yes.
    >>> str2bool_exc(None)
    ValueError: Cannot convert None to bool. ...

## API

### `str2bool(value, raise_exc=False, default=None)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `str \| bool \| int \| None` | Value to convert |
| `raise_exc` | `bool` | Raise `ValueError` on unrecognized input (default `False`) |
| `default` | `bool \| None` | Return value when input is unrecognized (default `None`) |

Raises `TypeError` for unsupported types (e.g. `float`, `list`).

### `str2bool_exc(value)`

Shorthand for `str2bool(value, raise_exc=True)`. Always raises `ValueError`
for `None` or unrecognized values.

## License
BSD

Forked from [symonsoft/str2bool](https://github.com/symonsoft/str2bool)
