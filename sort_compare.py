import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    """Perform insertion sort on the list."""
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value
    return time.time() - start_time


def shell_sort(a_list):
    """Perform shell sort on the list."""
    start_time = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count //= 2
    return time.time() - start_time


def gap_insertion_sort(a_list, start, gap):
    """Helper function for shell sort"""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap

        a_list[position] = current_value


def python_sort(a_list):
    """Use Python built-in sorted function."""
    start_time = time.time()
    sorted_list = sorted(a_list)
    return time.time() - start_time


def run_benchmark():
    """Run benchmark tests for sorting algorithms."""
    list_sizes = [500, 1000, 5000]

    for size in list_sizes:
        total_times = {"python_sort": 0, "insertion_sort": 0, "shell_sort": 0}

        for _ in range(100):
            random_list = get_me_random_list(size)

            # Python
            total_times["python_sort"] += python_sort(random_list[:])

            # Insertion 
            total_times["insertion_sort"] += insertion_sort(random_list[:])

            # Shell 
            total_times["shell_sort"] += shell_sort(random_list[:])

        print(f"List Size: {size}")
        print(f"Python sort took {total_times['python_sort'] / 100:.7f} seconds to run, on average")
        print(f"Insertion sort took {total_times['insertion_sort'] / 100:.7f} seconds to run, on average")
        print(f"Shell sort took {total_times['shell_sort'] / 100:.7f} seconds to run, on average")
        print("-" * 80)


if __name__ == "__main__":
    run_benchmark()
