'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


'''


# Function for matching two strings  
'''
Example:
strs = ['Sohail', 'Sohan', 'Soap']  on each iteration match untile the strs[i] != strs[j]
then concate the common words in both strs.

Match word by word

'''

def match_two_str(str1, str2):
    i, j = 0, 0
    result = ''
    while i < len(str1)-1 and j < len(str2)-1:
        if str1[i] != str2[j]:
            break
        result += str2[j]
        
        i += 1
        j += 1
        
    return result


def longestCommonPrefix(list_of_strings) -> str:
    initail_str = list_of_strings[0]           # Str1 
    
    for i in range(1, len(list_of_strings)):
        initail_str = match_two_str(initail_str, list_of_strings[i])
        
    return initail_str

if __name__ == "__main__":
    
    # list_of_strings = ['Sohail', 'Sohan', 'Soap']
    strs = ["flower","flow","flight"]
    print(f"Longest Common Prefix is {longestCommonPrefix(strs)}")