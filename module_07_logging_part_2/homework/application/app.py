import sys
import logging

from utils import string_to_operator

logger = logging.getLogger("calc_logger")
logging.basicConfig()
logger.setLevel('INFO')
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


def calc(args):
    logger.info(f"Arguments: {args}")
    print("Arguments: ", args)

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error(f"Error while converting number 1, error: {e}")
        print("Error while converting number 1")
        print(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error(f"Error while converting number 2, error: {e}")
        print("Error while converting number 1")
        print(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    print("Result: ", result)
    logger.info(f"Result: {result}")
    print(f"{num_1} {operator} {num_2} = {result}")
    logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    calc(sys.argv[1:])
