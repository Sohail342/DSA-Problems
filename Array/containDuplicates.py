'''
Given an array of intergers, return true if the array contains duplicates, otherwise return false.

'''

def containDuplicates(nums):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True
    
# Time complexity: O(n)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(containDuplicates(nums))
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print(containDuplicates(nums))