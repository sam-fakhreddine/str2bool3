from typing import Optional, Union

TRUE_SET = {'yes', 'true', 't', 'y', '1'}
FALSE_SET = {'no', 'false', 'f', 'n', '0'}


def str2bool(
    value: Optional[Union[str, bool, int]],
    raise_exc: bool = False,
    default: Optional[bool] = None,
) -> Optional[bool]:
    """Convert a string (or compatible type) to a boolean.

    Recognizes 'yes', 'true', 't', 'y', '1' as True and
    'no', 'false', 'f', 'n', '0' as False. Case-insensitive.
    Leading/trailing whitespace is stripped automatically.

    bool and int inputs are handled directly:
      - bool: returned as-is (True/False)
      - int 1: True, int 0: False, other ints: unrecognized

    Args:
        value: The value to convert. Strings, bools, ints, and None accepted.
        raise_exc: If True, raise ValueError for unrecognized values
                   (including None).
        default: Value to return when input is unrecognized and
                 raise_exc is False.

    Returns:
        True, False, or default.

    Raises:
        TypeError: If value is not str, bool, int, or None.
        ValueError: If value is unrecognized and raise_exc is True.
    """
    # bool must be checked before int (bool is a subclass of int)
    if isinstance(value, bool):
        return value

    if isinstance(value, int):
        if value == 1:
            return True
        if value == 0:
            return False
        if raise_exc:
            raise ValueError(
                f"Invalid integer value '{value}'. Expected 0 or 1."
            )
        return default

    if value is None:
        if raise_exc:
            raise ValueError(
                "Cannot convert None to bool. Expected one of: "
                + ', '.join(sorted(TRUE_SET | FALSE_SET)) + '.'
            )
        return default

    if not isinstance(value, str):
        raise TypeError(
            f"Expected str, bool, int, or None; got {type(value).__name__!r}."
        )

    value = value.strip().lower()

    if value in TRUE_SET:
        return True
    if value in FALSE_SET:
        return False

    if raise_exc:
        valid_values = ', '.join(sorted(TRUE_SET | FALSE_SET))
        raise ValueError(
            f"Invalid value '{value}'. Expected one of: {valid_values}."
        )

    return default


def str2bool_exc(value: Optional[Union[str, bool, int]]) -> bool:
    """Convert a string to boolean, raising ValueError for any invalid input.

    Equivalent to str2bool(value, raise_exc=True). None and unrecognized
    strings both raise ValueError.

    Raises:
        TypeError: If value is not str, bool, int, or None.
        ValueError: If value is None or not a recognized boolean string.
    """
    return str2bool(value, raise_exc=True)
