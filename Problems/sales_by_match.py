'''
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. 
The number of pairs is 2.

'''

# Sales by Match Problem

def sockMerchant(ar):
    counter = 0
    repeated = {}   
    for i in ar:
        if i in repeated:    
            repeated[i] += 1
        else:
            repeated[i] = 1
            
    dict_values = list(repeated.values())    # Convert the Occurances of values to list 
    repeated_values = list(filter(lambda x: x == 2 or x>2, dict_values)) # Filter all values that are equal to 2 or greater than 2 
    
    ''' 
    Iterate through filtered values and count them, 
    if value is 2 ( it means 1 paire of Socks) count 1,
    or if value is greater than 2 and is Even then division by 2 (6/2 = 3), count += 3 and 
    if value is odd then -1 from the value (9-1 = 8), then division by 2 (8/2= 4), count += 4. 
     
     ''' 
    for i in range(len(repeated_values)):
        if repeated_values[i] == 2:
            counter += 1
        elif repeated_values[i] % 2 == 0 and repeated_values[i] > 2 :
            even_num = repeated_values[i] / 2
            counter += even_num
        else:
            repeated_values[i] += -1
            differ_even = repeated_values[i] / 2
            counter += differ_even
    return int(counter)


# 2nd Solution using Inbuilt method Count 
def sockMerchant_(ar):
    count = 0
    set_arr = set(ar)
    for i in set_arr:
        count += ar.count(i)//2    # first count the occurance with floor division (5//2 = 2), then count each occurance
    return count 

if __name__ == "__main__":
    
    print(sockMerchant_([2,3,4,1,2,5,5,5]))   # Using Count method Output Should be 2
    
    print(sockMerchant([2,3,4,1,2,5,5,5]))  # Output Should be 2