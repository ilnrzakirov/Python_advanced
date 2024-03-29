import sys
import logging.config

import logging_tree

from log_conf import dict_conf

from utils import string_to_operator

logging.config.dictConfig(dict_conf)
logger = logging.getLogger("calc_logger")
with open("logging_tree.txt", "w") as file:
    file.write(logging_tree.format.build_description())
# logger.setLevel('INFO')
# handler = logging.StreamHandler(sys.stdout)
# datefmt = '%Y-%m-%d %H:%M:%S'
# formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s", datefmt=datefmt)
# handler.setFormatter(formatter)
# e_handler = logging.FileHandler("error.log")
# e_handler.setLevel(logging.ERROR)
# w_handler = logging.FileHandler("warning.log", "w")
# w_handler.setLevel(logging.WARNING)
# w_handler.setFormatter(formatter)
# i_handler = logging.FileHandler("info.log")
# i_handler.setFormatter(formatter)
# i_handler.setLevel(logging.INFO)
# logger.addHandler(w_handler)
# logger.addHandler(e_handler)
# logger.addHandler(i_handler)
# logger.addHandler(handler)

def calc(args):
    logger.info(f"Arguments: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error(f"Error while converting number 1, error: {e}")

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error(f"Error while converting number 2, error: {e}")

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    logger.info(f"Result: {result}")
    logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    calc(sys.argv[1:])
