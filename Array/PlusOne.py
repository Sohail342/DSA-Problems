'''
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are 
ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 2:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
digits does not contain any leading 0's.
0 <= digits[i] <= 9

'''




def plusOne(digits) -> list:
    for elements in range(len(digits)-1, -1, -1):  # iterate loop through reverse ( from last index )
        if digits[elements] < 9:
            digits[elements] += 1
            return digits
        digits[elements] = 0  # if value is 9, return 0 with [1]
    return [1] + digits


if __name__ == '__main__':
    
   print(plusOne([2,3,4,5,9]))
   
   
'''
Time Complexity

The algorithm involves iterating through the digits array from the last digit to the first.
So, the time complexity is O(n).

'''