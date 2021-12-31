import time

import pytest

from delayedqueue import DelayedQueue


@pytest.fixture
def delayedqueue():
    return DelayedQueue()


@pytest.fixture
def custom_time_func():
    return lambda: 1000


def test_delayedqueue_when_empty(delayedqueue):
    assert delayedqueue.is_empty() == True
    assert delayedqueue.peek() is None


def test_delayedqueue_ops(delayedqueue):
    assert delayedqueue.put("an item", 0) == True
    assert delayedqueue.peek() == "an item"
    assert delayedqueue.get() == "an item"

    with pytest.raises(ValueError):
        assert delayedqueue.put("test item", -1)


def test_delayedqueue_time_func(capfd, delayedqueue, custom_time_func):
    assert delayedqueue.time_func == time.time
    delayedqueue.time_func = custom_time_func
    assert delayedqueue.time_func() == 1000

    with pytest.raises(ValueError):
        delayedqueue.time_func = "definitely not a callable"

    delayedqueue.put("an item", 0)
    delayedqueue.time_func = custom_time_func
    out, err = capfd.readouterr()
    assert out.strip() == "Warning! updating time_func after enqueue. May result in unknown behaviour!"

