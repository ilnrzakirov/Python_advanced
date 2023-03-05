import logging
import random
import threading
import time
from typing import List

TOTAL_TICKETS: int = 10
ALL_PLACE = 100

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


class Director(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore, tickets_pool: int, seller_count: int) -> None:
        super(Director, self).__init__()
        self.sem: threading.Semaphore = semaphore
        self.all_tickets_in_pool = tickets_pool
        self.seller_count: int = seller_count

    def run(self) -> None:
        global TOTAL_TICKETS
        global ALL_PLACE
        while self.all_tickets_in_pool < ALL_PLACE:
            if TOTAL_TICKETS <= self.seller_count:
                with self.sem:
                    time.sleep(1)
                    if ALL_PLACE - self.all_tickets_in_pool < self.seller_count:
                        TOTAL_TICKETS += ALL_PLACE - self.all_tickets_in_pool
                        logger.info(f'{self.name} added {ALL_PLACE - self.all_tickets_in_pool} tickets')
                        self.all_tickets_in_pool += ALL_PLACE - self.all_tickets_in_pool
                    else:
                        TOTAL_TICKETS += self.seller_count
                        logger.info(f'{self.name} added {self.seller_count} tickets')
                        self.all_tickets_in_pool += self.seller_count


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.tickets_sold: int = 0
        logger.info('Seller started work')

    def run(self) -> None:
        global TOTAL_TICKETS
        is_running: bool = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.name} sold one;  {TOTAL_TICKETS} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self) -> None:
        time.sleep(random.randint(0, 1))


def main() -> None:
    semaphore: threading.Semaphore = threading.Semaphore()
    sellers: List[Seller | Director] = []
    director = Director(semaphore, TOTAL_TICKETS, 4)
    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)
    sellers.append(director)
    director.start()

    for seller in sellers:
        seller.join()
    logger.info(f"all sold tickets: {director.all_tickets_in_pool}")


if __name__ == '__main__':
    main()
