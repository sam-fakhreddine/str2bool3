from typing import Optional, Union

TRUE_VALUES: frozenset = frozenset({'yes', 'true', 't', 'y', '1', 'on', 'enabled'})
FALSE_VALUES: frozenset = frozenset({'no', 'false', 'f', 'n', '0', 'off', 'disabled'})

_VALID: str = ', '.join(sorted(TRUE_VALUES | FALSE_VALUES))
_MISSING = object()  # sentinel: value was not recognized

_Input = Optional[Union[str, bool, int]]


def _parse(value: _Input) -> object:
    """Coerce *value* to True, False, or _MISSING.

    Raises TypeError for unsupported types so callers never have to.
    """
    # bool must come before int — bool is a subclass of int
    if isinstance(value, bool):
        return value

    if isinstance(value, int):
        if value == 1:
            return True
        if value == 0:
            return False
        return _MISSING

    if value is None:
        return _MISSING

    if not isinstance(value, str):
        raise TypeError(
            f"Expected str, bool, int, or None; got {type(value).__name__!r}."
        )

    normalized = value.strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    return _MISSING


def str2bool(
    value: _Input,
    raise_exc: bool = False,
    default: Optional[bool] = None,
) -> Optional[bool]:
    """Convert a value to bool.

    Recognized True:  yes, true, t, y, 1, on, enabled
    Recognized False: no, false, f, n, 0, off, disabled

    Matching is case-insensitive; leading/trailing whitespace is stripped.
    bool inputs are passed through; int 1/0 map to True/False.

    Args:
        value:     Input to convert. Accepts str, bool, int, or None.
        raise_exc: Raise ValueError for unrecognized values (including None).
        default:   Returned when value is unrecognized and raise_exc is False.

    Returns:
        True, False, or default.

    Raises:
        TypeError: If value is not str, bool, int, or None.
        ValueError: If value is unrecognized and raise_exc is True.
    """
    result = _parse(value)
    if result is not _MISSING:
        return result  # type: ignore[return-value]

    if raise_exc:
        if value is None:
            raise ValueError(f"Cannot convert None to bool. Expected one of: {_VALID}.")
        if isinstance(value, int):
            raise ValueError(f"Invalid integer {value!r}. Expected 0 or 1.")
        raise ValueError(f"Invalid value {value!r}. Expected one of: {_VALID}.")

    return default


def str2bool_exc(value: _Input) -> bool:
    """Convert to bool, raising ValueError on any invalid input (including None).

    Shorthand for ``str2bool(value, raise_exc=True)``.

    Raises:
        TypeError: If value is not str, bool, int, or None.
        ValueError: If value is None or unrecognized.
    """
    return str2bool(value, raise_exc=True)
