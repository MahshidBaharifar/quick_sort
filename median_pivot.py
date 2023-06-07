import statistics
import random

def median_three_pivot(lst):
    if len(lst) == 0:
        return []
    
    numbers = [lst[0], lst[len(lst)//2], lst[-1]]  # Create a list of three numbers
    pivot = statistics.median(numbers)
    
    if pivot == lst[0]:
        index = 0
    elif pivot == lst[-1]:
        index = len(lst) - 1
    else:
        index = len(lst) // 2
    
    less = [num for num in lst[:index] + lst[index+1:] if num <= pivot]
    greater = [num for num in lst[:index] + lst[index+1:] if num > pivot]
    
    return median_three_pivot(less) + [pivot] + median_three_pivot(greater)



my_list=[random.randint(1,100) for  i in range(1,100)]
print(my_list)
print(median_three_pivot(my_list))


   