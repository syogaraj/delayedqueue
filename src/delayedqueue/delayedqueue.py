import threading
import time
from collections.abc import Callable
from typing import Callable as _Callable
from heapq import heappush, heappop

from delayedqueue.delayed_queue_item import DelayedQueueItem


class DelayedQueue:

    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.available = threading.Condition(self.lock)
        self.__time_func = time.time

    @property
    def time_func(self) -> _Callable:
        return self.__time_func

    @time_func.setter
    def time_func(self, func):
        if not isinstance(func, Callable):
            raise ValueError(f"time_func setter value [{func}] should be a callable")
        if self.queue:
            print("Warning! updating time_func after enqueue. May result in unknown behaviour!")
        self.__time_func = func

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def peek(self):
        with self.lock:
            if self.queue:
                return self.queue[0].item

    def put(self, item, delay: int) -> bool:
        if delay < 0:
            raise ValueError("delay must be a non-negative number")

        with self.available:
            wrapped_item = DelayedQueueItem(item, delay, self.__time_func)
            heappush(self.queue, wrapped_item)

            if self.queue[0] == wrapped_item:
                self.available.notify()
            return True

    def get(self):
        with self.lock:
            try:
                while True:
                    if not self.queue:
                        self.available.wait()
                    first = self.queue[0]
                    delay = first.get_delay()
                    if delay <= 0:
                        wrapped_item = heappop(self.queue)
                        return wrapped_item.item

                    self.available.wait(delay)
            finally:
                if self.queue:
                    self.available.notify()
