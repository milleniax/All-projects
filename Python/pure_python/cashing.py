import time
from functools import wraps


def cached(timeout, logged=False):
    """Decorator to cache the result of a function call.
    Cache expires after timeout seconds.
    """
    def decorator(func):
        if logged:
            print("-- Initializing cache for", func.__name__)
        cache = {}

        @wraps(func)
        def decorated_function(*args, **kwargs):
            if logged:
                print("-- Called function", func.__name__)
            key = args, frozenset(kwargs.items())
            result = None
            if key in cache:
                if logged:
                    print("-- Cache hit for", func.__name__, key)

                cache_hit, expiry = cache[key]
                if time.time() - expiry < timeout:
                    result = cache_hit
                elif logged:
                    print("-- Cache expired for", func.__name__, key)
            elif logged:
                print("-- Cache miss for", func.__name__, key)

            # No cache hit, or expired
            if result is None:
                result = func(*args, **kwargs)

            cache[key] = result, time.time()
            return result

        return decorated_function

    return decorator

@cached(10, True)
def fib(n):
    """Returns the n'th Fibonacci number."""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
for i in range(10):
    print(fib(i))