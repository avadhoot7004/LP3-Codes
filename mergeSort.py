import random, multiprocessing
from multiprocessing import Pool
from time import time

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def parallel_merge_sort(arr, workers):
    size = len(arr) // workers
    chunks = [arr[i*size:(i+1)*size] for i in range(workers)]
    chunks[-1] = arr[(workers-1)*size:]

    print("Starting parallel sort.")
    t = time()

    with Pool(workers) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)

    parallel_sort_time = time() - t

    print("Performing final merge.")
    t2 = time()

    while len(sorted_chunks) > 1:
        left = sorted_chunks.pop(0)
        right = sorted_chunks.pop(0)
        sorted_chunks.append(merge(left, right))

    final_merge_time = time() - t2

    return sorted_chunks[0], parallel_sort_time, final_merge_time

# ------------------- RUN TEST -------------------

if __name__ == "__main__":
    # Number of elements (adjust if RAM issues occur)
    n = 500000  

    cpus = multiprocessing.cpu_count()
    print(f"Using {cpus} cores")

    t = time()
    arr = [random.randint(0, 1_000_000) for _ in range(n)]
    print(f"List length: {len(arr)}")
    print(f"Random list generated in {time() - t:.6f}")

    arr_copy = arr[:]

    # Single Core
    t = time()
    sorted_single = merge_sort(arr)
    single_time = time() - t
    print(f"Single Core elapsed time: {single_time:.6f} sec")

    # Parallel
    sorted_parallel, parallel_time, merge_time = parallel_merge_sort(arr_copy, cpus)

    print(f"Final merge duration: {merge_time:.6f} sec")
    print(f"{cpus}-Core elapsed time: {parallel_time + merge_time:.6f} sec")

    # Verification
    print("Verification of sorting algorithm:", sorted_single == sorted(arr))
    print(f"Sorted arrays equal: {sorted_parallel == sorted(arr)}")
