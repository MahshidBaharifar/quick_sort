import time
import random
import matplotlib.pyplot as plt
from collections import defaultdict
my_elapsed_time=defaultdict(list)
def measure_time(func):
    def closure_func(lst):
        start_time = time.time()
        result=func(lst)
        end_time = time.time()
        elapsed_time = end_time - start_time
        my_elapsed_time[func.__name__].append(elapsed_time)
        return result

    return closure_func


def quicksort1(lst):
    if len(lst) < 2:
        return lst
    else:
        index = random.randint(0, len(lst) - 1)
        pivot = lst[index]
        less = [num for num in lst[:index]+lst[index+1:] if num <= pivot]
        greater = [num for num in lst[:index]+lst[index+1:] if num > pivot]

    return quicksort1(less) + [pivot] + quicksort1(greater)

@measure_time
def wrapper1(lst):
    quicksort1(lst)
    


def quicksort2(lst):
    if len(lst) < 2:
        return lst  #[2]
    else:
        pivot = lst[1]
        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
      

    return quicksort2(less) + [pivot] + quicksort2(greater) 


@measure_time
def wrapper2(lst):
    quicksort2(lst)





times1 = []
times2 = []
X = range(1, 1001)
X = [num for num in X if num % 4 == 0]
for num in X:
    
    my_list1=list(range(num))
    random.shuffle(my_list1)
    wrapper1(my_list1)


for num in X:
    my_list2=list(range(num))
    random.shuffle(my_list2)
    wrapper2(my_list2)
   

plt.plot(X, my_elapsed_time['wrapper1'], color='r', label='non_rand', linestyle='solid')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()


plt.plot(X, my_elapsed_time['wrapper2'], color='g', label='rand', linestyle='solid')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()