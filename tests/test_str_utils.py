import pytest
from str2bool3 import FALSE_VALUES, TRUE_VALUES, str2bool, str2bool_exc


# ---------------------------------------------------------------------------
# Public constants
# ---------------------------------------------------------------------------

class TestValueSets:
    def test_true_values_is_frozenset(self):
        assert isinstance(TRUE_VALUES, frozenset)

    def test_false_values_is_frozenset(self):
        assert isinstance(FALSE_VALUES, frozenset)

    def test_true_and_false_sets_are_disjoint(self):
        assert TRUE_VALUES.isdisjoint(FALSE_VALUES)

    def test_true_values_contains_expected(self):
        assert {'yes', 'true', 't', 'y', '1', 'on', 'enabled'} <= TRUE_VALUES

    def test_false_values_contains_expected(self):
        assert {'no', 'false', 'f', 'n', '0', 'off', 'disabled'} <= FALSE_VALUES


# ---------------------------------------------------------------------------
# str2bool — true values
# ---------------------------------------------------------------------------

class TestTrueValues:
    @pytest.mark.parametrize("value", [
        "yes", "YES", "Yes", "yEs",
        "true", "True", "TRUE", "tRuE",
        "t", "T",
        "y", "Y",
        "1",
        "on", "ON", "On",
        "enabled", "ENABLED", "Enabled",
    ])
    def test_string_true(self, value):
        assert str2bool(value) is True

    def test_bool_true_passthrough(self):
        assert str2bool(True) is True

    def test_int_one(self):
        assert str2bool(1) is True


# ---------------------------------------------------------------------------
# str2bool — false values
# ---------------------------------------------------------------------------

class TestFalseValues:
    @pytest.mark.parametrize("value", [
        "no", "NO", "No", "nO",
        "false", "False", "FALSE", "fAlSe",
        "f", "F",
        "n", "N",
        "0",
        "off", "OFF", "Off",
        "disabled", "DISABLED", "Disabled",
    ])
    def test_string_false(self, value):
        assert str2bool(value) is False

    def test_bool_false_passthrough(self):
        assert str2bool(False) is False

    def test_int_zero(self):
        assert str2bool(0) is False


# ---------------------------------------------------------------------------
# str2bool — whitespace handling
# ---------------------------------------------------------------------------

class TestWhitespace:
    def test_leading_space_true(self):
        assert str2bool(" yes") is True

    def test_trailing_space_true(self):
        assert str2bool("yes ") is True

    def test_both_spaces_true(self):
        assert str2bool("  yes  ") is True

    def test_tab_whitespace_true(self):
        assert str2bool("\tyes\t") is True

    def test_leading_space_false(self):
        assert str2bool(" no") is False

    def test_trailing_space_false(self):
        assert str2bool("no ") is False

    def test_both_spaces_false(self):
        assert str2bool("  no  ") is False

    def test_whitespace_around_on(self):
        assert str2bool("  on  ") is True

    def test_whitespace_around_disabled(self):
        assert str2bool("  disabled  ") is False


# ---------------------------------------------------------------------------
# str2bool — None and defaults
# ---------------------------------------------------------------------------

class TestNoneAndDefaults:
    def test_none_returns_none_by_default(self):
        assert str2bool(None) is None

    def test_none_with_custom_default_true(self):
        assert str2bool(None, default=True) is True

    def test_none_with_custom_default_false(self):
        assert str2bool(None, default=False) is False

    def test_invalid_string_returns_none_by_default(self):
        assert str2bool("maybe") is None

    def test_invalid_string_with_custom_default(self):
        assert str2bool("maybe", default=False) is False

    def test_empty_string_returns_none(self):
        assert str2bool("") is None

    def test_empty_string_with_default(self):
        assert str2bool("", default=True) is True

    def test_invalid_int_returns_none(self):
        assert str2bool(2) is None

    def test_invalid_int_with_default(self):
        assert str2bool(2, default=False) is False


# ---------------------------------------------------------------------------
# str2bool — raise_exc=True
# ---------------------------------------------------------------------------

class TestRaiseExc:
    def test_valid_true_no_exception(self):
        assert str2bool("yes", raise_exc=True) is True

    def test_valid_false_no_exception(self):
        assert str2bool("no", raise_exc=True) is False

    def test_on_no_exception(self):
        assert str2bool("on", raise_exc=True) is True

    def test_disabled_no_exception(self):
        assert str2bool("disabled", raise_exc=True) is False

    def test_bool_true_no_exception(self):
        assert str2bool(True, raise_exc=True) is True

    def test_bool_false_no_exception(self):
        assert str2bool(False, raise_exc=True) is False

    def test_int_one_no_exception(self):
        assert str2bool(1, raise_exc=True) is True

    def test_int_zero_no_exception(self):
        assert str2bool(0, raise_exc=True) is False

    def test_none_raises_value_error(self):
        with pytest.raises(ValueError):
            str2bool(None, raise_exc=True)

    def test_invalid_string_raises_value_error(self):
        with pytest.raises(ValueError):
            str2bool("maybe", raise_exc=True)

    def test_empty_string_raises_value_error(self):
        with pytest.raises(ValueError):
            str2bool("", raise_exc=True)

    def test_invalid_int_raises_value_error(self):
        with pytest.raises(ValueError):
            str2bool(2, raise_exc=True)

    def test_error_message_contains_invalid_value(self):
        with pytest.raises(ValueError, match="maybe"):
            str2bool("maybe", raise_exc=True)

    def test_error_message_mentions_expected_values(self):
        with pytest.raises(ValueError, match="Expected one of"):
            str2bool("nope", raise_exc=True)

    def test_none_error_mentions_expected_values(self):
        with pytest.raises(ValueError, match="Expected one of"):
            str2bool(None, raise_exc=True)

    def test_invalid_int_error_mentions_zero_one(self):
        with pytest.raises(ValueError, match="0 or 1"):
            str2bool(2, raise_exc=True)


# ---------------------------------------------------------------------------
# str2bool — TypeError for unsupported types
# ---------------------------------------------------------------------------

class TestTypeError:
    @pytest.mark.parametrize("value", [
        1.0,
        [],
        {},
        object(),
        b"yes",
    ])
    def test_unsupported_type_raises_type_error(self, value):
        with pytest.raises(TypeError):
            str2bool(value)

    def test_type_error_message_includes_type_name(self):
        with pytest.raises(TypeError, match="float"):
            str2bool(1.0)


# ---------------------------------------------------------------------------
# str2bool_exc
# ---------------------------------------------------------------------------

class TestStr2BoolExc:
    def test_valid_true(self):
        assert str2bool_exc("yes") is True

    def test_valid_false(self):
        assert str2bool_exc("no") is False

    def test_on(self):
        assert str2bool_exc("on") is True

    def test_off(self):
        assert str2bool_exc("off") is False

    def test_enabled(self):
        assert str2bool_exc("enabled") is True

    def test_disabled(self):
        assert str2bool_exc("disabled") is False

    def test_bool_true_passthrough(self):
        assert str2bool_exc(True) is True

    def test_bool_false_passthrough(self):
        assert str2bool_exc(False) is False

    def test_int_one(self):
        assert str2bool_exc(1) is True

    def test_int_zero(self):
        assert str2bool_exc(0) is False

    def test_none_raises(self):
        with pytest.raises(ValueError):
            str2bool_exc(None)

    def test_invalid_string_raises(self):
        with pytest.raises(ValueError):
            str2bool_exc("invalid")

    def test_invalid_int_raises(self):
        with pytest.raises(ValueError):
            str2bool_exc(2)

    def test_whitespace_true(self):
        assert str2bool_exc(" yes ") is True

    def test_whitespace_false(self):
        assert str2bool_exc(" no ") is False

    def test_whitespace_on(self):
        assert str2bool_exc(" on ") is True

    def test_whitespace_disabled(self):
        assert str2bool_exc(" disabled ") is False

    def test_unsupported_type_raises_type_error(self):
        with pytest.raises(TypeError):
            str2bool_exc(1.0)
