from typing import Optional

TRUE_SET = {'yes', 'true', 't', 'y', '1'}
FALSE_SET = {'no', 'false', 'f', 'n', '0'}

def str2bool(value: Optional[str], raise_exc: bool = False, default: Optional[bool] = None) -> Optional[bool]:
    if value is None:
        return default
    
    value = value.lower()
    if value in TRUE_SET:
        return True
    if value in FALSE_SET:
        return False
    
    if raise_exc:
        valid_values = ', '.join(sorted(TRUE_SET | FALSE_SET))
        raise ValueError(f"Invalid value '{value}'. Expected one of: {valid_values}.")
    
    return default

def str2bool_exc(value: Optional[str]) -> bool:
    return str2bool(value, raise_exc=True)
