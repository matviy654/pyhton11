#task1
# def product_of_elements(nums):
#     product = 1
#     for num in nums:
#         product *= num
#     return product

# numbers = [1, 2, 3, 4, 5]
# result = product_of_elements(numbers)
# print("Добуток елементів списку:", result)

#task2
# def find_minimum(nums):
#     if not nums:
#         return None  
#     minimum = nums[0]
#     for num in nums:
#         if num < minimum:
#             minimum = num
#     return minimum

# numbers = [4, 2, 8, 1, 5]
# result = find_minimum(numbers)
# print("Мінімум у списку:", result)

#task3
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def count_primes(nums):
#     prime_count = 0
#     for num in nums:
#         if is_prime(num):
#             prime_count += 1
#     return prime_count

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# result = count_primes(numbers)
# print("Кількість простих чисел у списку:", result)

#task4
# def remove_elements(nums, val):
#     original_length = len(nums)
#     nums[:] = [num for num in nums if num != val]
#     removed_count = original_length - len(nums)
#     return removed_count

# numbers = [3, 2, 2, 3, 4, 5, 3]
# value_to_remove = 3
# deleted_count = remove_elements(numbers, value_to_remove)
# print("Кількість видалених елементів:", deleted_count)
# print("Список після видалення:", numbers)

#task5
# def merge_lists(list1, list2):
#     return list1 + list2

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = merge_lists(list1, list2)
# print("Об'єднаний список:", result)

#task6
# def power_list(nums, power):
#     powered_list = [num ** power for num in nums]
#     return powered_list
# numbers = [1, 2, 3, 4, 5]
# degree = 3
# powered_numbers = power_list(numbers, degree)
# print("Список чисел піднесений до ступеня {}: {}".format(degree, powered_numbers))
