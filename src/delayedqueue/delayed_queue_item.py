"""
Wrapper for the item which is going to be enqueued in the queue.
"""


class DelayedQueueItem:
    def __init__(self, item, delay, time_func):
        self.item = item
        self.delay = delay
        self.time_func = time_func
        self.target_time = int(self.time_func() * 1000) + delay * 1000

    def get_delay(self) -> int:
        return (self.target_time - int(self.time_func() * 1000)) / 1000

    def __lt__(self, other) -> bool:
        if not isinstance(other, DelayedQueueItem):
            raise ValueError("comparison should be made between same types")
        return self.target_time <= other.target_time

    def __eq__(self, other) -> bool:
        if not isinstance(other, DelayedQueueItem):
            raise ValueError("comparison should be made between same types")
        return self.item == other.item and self.delay == other.delay and self.target_time == other.target_time

    def __repr__(self) -> str:
        return f"""(Item: {self.item}, Delay: {self.delay}, Time Func: {self.time_func}, Next Execution Time: {self.target_time}"""
