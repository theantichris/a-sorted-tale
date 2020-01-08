import random

def bubble_sort(list):
  swaps = 0
  sorted = False

  while not sorted:
    sorted = True

    for idx in range(len(list) - 1):
      if list[idx] > list[idx + 1]:
        sorted = False
        list[idx], list[idx + 1] = list[idx + 1], list[idx]
        swaps += 1

  print("Bubble sort: There were {0} swaps".format(swaps))

  return list

def quicksort(list, start, end):
  if start >= end:
    return

  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]

  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  less_than_pointer = start
  
  for i in range(start, end):
    if pivot_element > list[i]:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)