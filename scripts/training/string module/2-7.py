'''
Дана строка '0123456789'. Удалите из нее первый, пятый и
последний символы. Выведите результат на экран.
'''

nums = '0123456789'
print(nums[1:4] + nums[5:9])
nums = nums.replace('0', '')
nums = nums.replace('4', '')
nums = nums.replace('9', '')
print(nums)
