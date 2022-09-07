import logging
from typing import Union, Callable
from operator import sub, mul, add

utils_logger = logging.getLogger("utils_logger")

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        utils_logger.error(f"wrong operator type, value={value}")
        print("wrong operator type", value)
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        utils_logger.error(f"wrong operator value, value={value}")
        print("wrong operator value", value)
        raise ValueError("wrong operator value")

    return OPERATORS[value]
