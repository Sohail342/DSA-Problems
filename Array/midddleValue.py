'''
Find Middle Value from the array

Example 1:  ( length of array is odd)
arr = [7,6,4,3,1]
Output: i = 4, j = 4
Middle Value is 4

Example 2:  ( length of array is even)
arr = [1,4,8,3,5,6]
Output: i = 8, j = 3
Middle values are = 8, 3
'''

# First Approach with O(n) Time Complexity
def midddleValue(arr) -> int:
    i, j = 0, len(arr)-1
    while i < len(arr) and j != -1:
        
        if i == j:
            print(arr[i])
            break
        elif i == j - 1:
            print(arr[i], arr[j])
            break
        
        i += 1; j -= 1
        
''' The time complexity of this function is O(n), where n is the number of elements in the array. 

1. The function has two pointers, i and j, that start at the beginning and end of the array, respectively.
2. In each iteration, both i and j move toward the center (one step inward per iteration).
3. This loop runs until i == j, meaning it runs for roughly n/2 iterations, where n is the length of the array. ( in Case of Odd Length of array)
4. If i == j - 1, it prints the two middle elements. ( in Case of even length of array).
5. Since constants are ignored in Big-O notation, the time complexity is considered O(n).

'''

# Second Approach with O(1) Time Complexity
def midddleValue_second(arr):
    middle_value = len(arr) // 2
    if middle_value % 2 == 0:
        value_one = arr[middle_value]
        value_two = arr[middle_value-1]
        print(value_two, value_one) 
    else:
        print(arr[middle_value])
        
'''
The time complexity here is O(1) (constant time), 
since it simply involves accessing an element from the array using its index.

This approach is much faster since it avoids looping altogether.

'''
    
if __name__ == '__main__':
    
    midddleValue([7,6,4,3,1,8, 9, 7])              # Output 3 1 with Time Complexity O(n)
    midddleValue_second([7,6,4,3,1,8, 9, 7])       # Output 3 1 with Time Complexity O(1)