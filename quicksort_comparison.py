import random
import time
import matplotlib.pyplot as plt

# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Детермінований QuickSort (опорний елемент - середній)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Генерація тестових масивів
sizes = [10_000, 50_000, 100_000, 500_000]
num_tests = 5
results = []

for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    
    # Вимірюємо час для рандомізованого QuickSort
    rand_times = []
    for _ in range(num_tests):
        arr_copy = test_array[:]
        start_time = time.time()
        randomized_quick_sort(arr_copy)
        rand_times.append(time.time() - start_time)
    avg_rand_time = sum(rand_times) / num_tests
    
    # Вимірюємо час для детермінованого QuickSort
    det_times = []
    for _ in range(num_tests):
        arr_copy = test_array[:]
        start_time = time.time()
        deterministic_quick_sort(arr_copy)
        det_times.append(time.time() - start_time)
    avg_det_time = sum(det_times) / num_tests
    
    results.append((size, avg_rand_time, avg_det_time))
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {avg_rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {avg_det_time:.4f} секунд\n")

# Візуалізація результатів
sizes, rand_times, det_times = zip(*results)
plt.figure(figsize=(10, 5))
plt.plot(sizes, rand_times, label='Рандомізований QuickSort', marker='o')
plt.plot(sizes, det_times, label='Детермінований QuickSort', marker='s')
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння швидкості QuickSort")
plt.legend()
plt.grid()
plt.show()
