import time
import random

numbers = []
searchnumbers = []

for i in range(10000):
  numbers.append(random.randint(0,100000))

for i in range(1000):
  searchnumbers.append(random.randint(0,100000))

def binSearchIter(lst, item):
  low = 0
  high = len(lst) - 1
  while low <= high:
    mid = (high + low) // 2
    x = lst[mid]
    
    if x == item:
      return True
    elif x < item:          # Cannot be on left side
      low = mid + 1
    else:                   # x > item, cannot be on right side
      high = mid - 1
  
  return False

def binSearchRecur(lst, item):
  high = len(lst) - 1
  if high < 0:              # The list is empty
    return False
  
  mid = high // 2
  if lst[mid] == item:
    return True
  elif lst[mid] < item:
    # We already know that item is not at mid, so we exclude mid
    return binSearchRecur(lst[mid + 1:], item) 
  else:
    return binSearchRecur(lst[:mid], item) 

def LinearSearch(lst,item):
  for i in lst:
    if i == item:
      return True
  return False

start = time.time()
for i in range(1000):
  LinearSearch(numbers, searchnumbers[i])
finish = time.time()
print(f'linear search:{finish-start}')

numbers.sort()