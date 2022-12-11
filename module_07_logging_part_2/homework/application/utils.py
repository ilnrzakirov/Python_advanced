import logging.config
import sys
from typing import Union, Callable
from operator import sub, mul, add
from log_conf import dict_conf

logging.config.dictConfig(dict_conf)
utils_logger = logging.getLogger("utils_logger")
# utils_logger.setLevel('INFO')
# handler = logging.StreamHandler(sys.stdout)
# datefmt = '%Y-%m-%d %H:%M:%S'
# formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s", datefmt=datefmt)
# handler.setFormatter(formatter)
# utils_logger.addHandler(handler)


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
        utils_logger.warning(f"wrong operator type, value={value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        utils_logger.warning(f"wrong operator value, value={value}")
        raise ValueError("wrong operator value")

    return OPERATORS[value]
