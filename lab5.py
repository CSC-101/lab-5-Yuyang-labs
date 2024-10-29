import data
from data import (Time)
from data import Point
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3

def time_add(time1:Time, time2:Time) -> Time:
    time_second = time1.second + time2.second
    time_minute = time1.minute + time2.minute
    time_hour = time1.hour + time2.hour
    time_total = Time(time_minute//60 + time_hour, time_second//60 + time_minute % 60, time_second % 60 )
    return time_total



# Part 4
def is_descending(list1:list[float])-> bool:
    for i in range(len(list1)-1):
        for j in range(len(list1) - i - 1):
            if list1[j]>list1[j+1]:
                num = list1[j]
                list1[j] = list1[j+1]
                list1[j] = num
                return True
    else:
        return False

# Part 5

def largest_between(list_num:list[int], lower_idx:int, upper_idx:int)-> int:

    if upper_idx > len(list_num):
        upper_idx = len(list_num) -1

    elif lower_idx < 0:
        lower_idx = 0

    elif lower_idx >= upper_idx:
        return None


    largest_idx = None
    largest_value = None
    for num in range(lower_idx, upper_idx + 1):
        current_value = list_num[num]
        if largest_value is None or current_value > largest_value:
            largest_value = current_value
            largest_idx = num
    return largest_idx





# Part 6

def furthest_from_origin(list1:list[Point]):
    if not list1:
        return None
    furthest_idx = 0
    max_distance_squared = list1[0].x ** 2 + list1[0].y ** 2
    for idx in range(1, len(list1)):
        distance_squared = list1[idx].x**2 + list1[idx].y**2
        if distance_squared > max_distance_squared:
            max_distance_squared = distance_squared
            furthest_idx = idx
    return furthest_idx


