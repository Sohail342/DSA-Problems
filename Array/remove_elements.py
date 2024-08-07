'''
Remove all the occurance of praticular element for the array or list.

The function iterates through the list nums and appends elements that 
are not equal to val to the removed_list and skip the iteration where val is equal to array elemet. 
Finally, it returns the removed_list.


Initialization of removed_list: This takes constant time, O(1).
Loop through nums: The function iterates over each element in the list nums, which has 𝑛 elements. This loop runs in O(n) time.
Condition check if nums[i] == val: This comparison is performed for each element and takes constant time, O(1).
Appending to removed_list: Appending an element to a list generally takes amortized constant time, O(1).

Thus, the overall time complexity of the removeElement() is O(n), where 𝑛
is the number of elements in the input list nums. 

'''

def removeElement(nums, val) -> list:

    removed_list = []
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        
        removed_list.append(nums[i])
        
    return removed_list

if __name__ == "__main__":
    
    print(removeElement([2,5,6,7,3,4,2], 5))