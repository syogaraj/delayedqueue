import time
from collections.abc import Callable

import pytest
from delayedqueue.delayed_queue_item import DelayedQueueItem


@pytest.fixture
def time_func():
    return time.time


@pytest.fixture
def delayed_queue_item(time_func):
    return DelayedQueueItem(item="an item", delay=10, time_func=time_func)


@pytest.fixture
def another_delayed_queue_item(time_func):
    return DelayedQueueItem(item="another item", delay=10, time_func=time_func)


def test_delayed_queue_item(time_func, delayed_queue_item, another_delayed_queue_item):
    assert delayed_queue_item.item == "an item"
    assert delayed_queue_item.delay == 10
    assert isinstance(time_func, Callable)

    assert delayed_queue_item != another_delayed_queue_item
    assert delayed_queue_item < another_delayed_queue_item


def test_delayed_queue_item_raise_errs(delayed_queue_item, another_delayed_queue_item):
    with pytest.raises(ValueError):
        assert delayed_queue_item == 10

    with pytest.raises(ValueError):
        assert another_delayed_queue_item < 10


def test_delayed_queue_item_delay(delayed_queue_item):
    item_delay = delayed_queue_item.get_delay()
    assert type(item_delay) == float
    assert (delayed_queue_item.target_time - int(delayed_queue_item.time_func() * 1000)) / 1000 == item_delay
