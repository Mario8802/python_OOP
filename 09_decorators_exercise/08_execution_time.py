from time import time

# with stop
# def exec_time(func):
#     def wrapper(*args, **kwargs):
#         start = time()  # gets the current time
#         func(*args, start_time=start, threshold=2, **kwargs)
#         end = time()  # gets the current time
#
#         return end - start
#
#     return wrapper
#
#
# @exec_time
# def loop(start, end, start_time, threshold):
#     total = 0
#
#     for x in range(start, end):
#         if time() - start_time > threshold:
#             print("function terminated")
#             return
#
#         total += x
#
#     return total


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time()  # gets the current time
        func(*args, **kwargs)
        end = time()  # gets the current time

        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0

    for x in range(start, end):
        total += x

    return total


@exec_time
def concatenate(strings):
    result = ""

    for string in strings:
        result += string

    return result


print(concatenate(["a" for i in range(100_000_000)]))


# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function {func.__name__!r} took: {end_time - start_time:.2f} seconds")
#         return result

#     return wrapper

# @timer
# def example_function(n):
#     return f"The sun is {sum(range(n))}"


# example_function = timer(example_function)


# print(example_function(1000000000))