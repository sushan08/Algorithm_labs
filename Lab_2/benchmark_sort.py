import matplotlib.pyplot as plt
import timeit
from sort import merge_sort, quick_sort
import random

def plot(x, y, label):
    plt.plot(x, y, label=label)

def get_time():
    input_size = []
    merge_time = []
    quick_time = []
    for n in range(10000, 100000, 10000):
        total_merge_time = 0
        total_quick_time = 0
        random_list = list(range(0, n+1))
        random.shuffle(random_list)

        # mergeSort time
        start = timeit.default_timer()
        merge_sort(random_list, 0, len(random_list) - 1)
        end = timeit.default_timer()
        time_taken_merge = end - start

        # quickSort time
        start = timeit.default_timer()
        random.shuffle(random_list)
        quick_sort(random_list, 0, len(random_list) - 1)
        end = timeit.default_timer()
        time_taken_quick = end - start

        merge_time.append(time_taken_merge)
        quick_time.append(time_taken_quick)
        input_size.append(n)
        total_merge_time += time_taken_merge
        total_quick_time += time_taken_quick

    plt.title("Time Complexity Curve", loc='left')
    plt.xlabel("Size of array")
    plot(input_size, merge_time, label="MergeSort")
    plot(input_size, quick_time, label="QuickSort")
    plt.legend()
    plt.ylabel("Running time in ns")
    plt.show()

if __name__ == "__main__":
    get_time()