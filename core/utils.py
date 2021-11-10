from time import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def _func(*args, **kwargs):
        t = time()
        _res = func(*args, **kwargs)
        return time() - t, _res
    return _func
