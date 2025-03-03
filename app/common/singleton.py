from functools import wraps
import threading


def singleton(cls):
    orig_new = cls.__new__
    instance = None
    lock = threading.Lock()

    @wraps(cls.__new__)
    def __new__(new_cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            with lock:
                if instance is None:
                    instance = orig_new(new_cls, *args, **kwargs)
        return instance

    cls.__new__ = __new__
    return cls
