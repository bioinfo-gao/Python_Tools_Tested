def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"缓存命中: {args}")
            print(f"缓存值是: {cache[args]}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 第二次调用会用缓存！