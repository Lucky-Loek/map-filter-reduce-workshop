from functools import reduce

# 1. Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
lst = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x**2, lst)))

# 2. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
evenFiltered = list(filter(lambda x: x % 2 == 0, lst))
print(list(map(lambda x: x**2, evenFiltered)))

# 3. Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
evenFilteredBelowTwenty = list(filter(lambda x: x % 2 == 0, range(1,21)))
print(evenFilteredBelowTwenty)

# 4. Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
print(list(map(lambda x: x**2, range(1,21))))

# 5. Determine the maximum of a list of numerical values by using reduce.
print(reduce(lambda largest, current: largest if (largest > current) else current, range(1,21)))

# 6. Calculate the sum of the numbers from 1 to 100, use reduce.
print(reduce(lambda previous, current: previous + current, range(1,101)))

# 7. Change the previous example to calculate the product (the factorial) from 1 to a number, but do not choose 50. 
print(reduce(lambda previous, current: previous * current, range(1,21)))

# 8. Write a Python program to filter the positive numbers from a list.
print(list(filter(lambda x: x > 0, range(-10, 10))))

# 9. Find the intersection of two lists, using filter.
lst2 = [5,6,7,8,9,10,11,12,13,14,15]
print(list(filter(lambda x: x in lst2, lst)))
print([x for x in lst if x in lst2])