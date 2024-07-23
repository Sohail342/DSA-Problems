'''
Problem: Length of Last Word

Given a string 'string' consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.


Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

'''


def lengthOfLastWord(string:str):
    split_array = string.split()   # split string to list
    last_word = split_array[-1]    # Fetch Last Index

    return len(last_word)


if __name__ == "__main__":
    
    print(lengthOfLastWord("My Name is Sohail"))