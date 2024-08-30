from typing import Optional

class StrUtils:
    TRUE_SET = {'yes', 'true', 't', 'y', '1'}
    FALSE_SET = {'no', 'false', 'f', 'n', '0'}

    @staticmethod
    def str2bool(value: Optional[str], raise_exc: bool = False, default: Optional[bool] = None) -> Optional[bool]:
        if value is None:
            return default

        value = value.lower()
        if value in StrUtils.TRUE_SET:
            return True
        if value in StrUtils.FALSE_SET:
            return False

        if raise_exc:
            valid_values = ', '.join(sorted(StrUtils.TRUE_SET | StrUtils.FALSE_SET))
            raise ValueError(f"Invalid value '{value}'. Expected one of: {valid_values}.")

        return default

    @staticmethod
    def str2bool_exc(value: Optional[str]) -> bool:
        return StrUtils.str2bool(value, raise_exc=True)
