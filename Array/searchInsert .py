'''

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where 
it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''


def searchInsert(nums, target) -> int:
    try:
        return nums.index(target)
    except:
        nums.append(target)
        nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    
    print(searchInsert([1,3,5,6], 5))
    
    
'''
Overall Time Complexity:
1. If the target is found in nums, the function simply returns nums.index(target), 
   so the time complexity in this case is O(n).
   
2. If the target is not found in nums, the time complexity is dominated by the 
   sorting operation, which is O(nlogn).

'''
