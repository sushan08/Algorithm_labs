import matplotlib.pyplot as plt
from search import linear_search, binary_search
import timeit

def plot(x, y, label):
    plt.plot(x, y, label=label)

def get_time():
    input_size = []
    binarysearch_time = []
    linearsearch_time = []
    for n in range(10000, 100000, 10000):
        total_binary_time = 0
        total_linear_time = 0
        random_list = list(range(0, n+1))


# binarySearch time
        start = timeit.default_timer()
        a = binary_search(random_list, -1)
        end = timeit.default_timer()
        time_taken_binary = end - start


# linearSearch time
        start = timeit.default_timer()
        a = linear_search(random_list, -1)
        end = timeit.default_timer()
        time_taken_linear = end - start

        binarysearch_time.append(time_taken_binary)
        linearsearch_time.append(time_taken_linear)
        input_size.append(n)
        total_binary_time += time_taken_binary
        total_linear_time += time_taken_linear

    plt.title("Time Complexity Curve", loc='left')
    plt.xlabel("Size of array")
    plot(input_size, linearsearch_time, label="LinearSearch")
    plot(input_size, binarysearch_time, label="BinarySearch")
    plt.legend()
    plt.ylabel("Running time in ns")
    plt.show()

if __name__ == "__main__":
    get_time()