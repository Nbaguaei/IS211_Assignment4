import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order."""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    """Sequential search for an item in an unordered list."""
    start_time = time.time()
    for element in a_list:
        if element == item:
            return True, time.time() - start_time
    return False, time.time() - start_time


def ordered_sequential_search(a_list, item):
    """Ordered sequential search in a sorted list."""
    start_time = time.time()
    for element in a_list:
        if element == item:
            return True, time.time() - start_time
        elif element > item:
            break
    return False, time.time() - start_time


def binary_search_iterative(a_list, item):
    """Binary search (iterative) on a sorted list."""
    start_time = time.time()
    first, last = 0, len(a_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True, time.time() - start_time
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False, time.time() - start_time


def binary_search_recursive(a_list, item, start_time=None):
    """Binary search (recursive) on a sorted list."""
    if start_time is None:
        start_time = time.time()

    if len(a_list) == 0:
        return False, time.time() - start_time

    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True, time.time() - start_time
    elif item < a_list[midpoint]:
        return binary_search_recursive(a_list[:midpoint], item, start_time)
    else:
        return binary_search_recursive(a_list[midpoint + 1:], item, start_time)


def run_benchmark():
    """Runs search benchmarks for different list sizes."""
    sizes = [500, 1000, 5000]
    target = 99999999  

    for size in sizes:
        total_times = {
            "sequential": 0, "ordered_sequential": 0,
            "binary_iterative": 0, "binary_recursive": 0
        }

        for _ in range(100):
            mylist = get_me_random_list(size)
            sorted_list = sorted(mylist)

            # Sequential 
            _, t = sequential_search(mylist, target)
            total_times["sequential"] += t

            # Ordered Sequential
            _, t = ordered_sequential_search(sorted_list, target)
            total_times["ordered_sequential"] += t

            # Binary Search 
            _, t = binary_search_iterative(sorted_list, target)
            total_times["binary_iterative"] += t

            # Binary Search 
            _, t = binary_search_recursive(sorted_list, target)
            total_times["binary_recursive"] += t

        print(f"List Size: {size}")
        print(f"Sequential Search took {total_times['sequential'] / 100:.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {total_times['ordered_sequential'] / 100:.7f} seconds to run, on average")
        print(f"Binary Search (Iterative) took {total_times['binary_iterative'] / 100:.7f} seconds to run, on average")
        print(f"Binary Search (Recursive) took {total_times['binary_recursive'] / 100:.7f} seconds to run, on average")
        print("-" * 80)


if __name__ == "__main__":
    run_benchmark()
