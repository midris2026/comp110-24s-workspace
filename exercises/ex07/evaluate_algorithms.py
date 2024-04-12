__author__ = "730569217"

import matplotlib.pyplot as plt
from exercises.ex07.runtime_analysis_functions import evaluate_runtime, evaluate_memory_usage

start_size: int = 0
end_size: int = 1000

times = evaluate_runtime("selection_sort", start_size, end_size)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - MIDRIS")
plt.show()

times = evaluate_runtime("insertion_sort", start_size, end_size)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - MIDRIS")
plt.show()

usage = evaluate_memory_usage("selection_sort", start_size, end_size)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - MIDRIS")
plt.show()

usage = evaluate_memory_usage("insertion_sort", start_size, end_size)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - MIDRIS")
plt.show()