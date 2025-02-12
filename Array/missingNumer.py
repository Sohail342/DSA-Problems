'''
Give a array nums cotaining n distinct numbers taken from 0, 1, 2, ..., n, return the one that is missing from the array.

'''


def missingNumber(nums):
    set_nums = set(nums)
    
    for i in range(min(nums), max(nums)):
        if i not in set_nums:
            return i
    else:
        return None
            
        

if __name__ == '__main__':
    print(missingNumber([3, 0, 1]))