'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

'''

def  valid_palindrome(s) -> bool:
   i, j = 0, len(s) - 1
   while i < j:
      if not s[i].isalnum():
            i += 1
      elif not s[j].isalnum():
            j -= 1
      elif s[i].lower() != s[j].lower():
            return False
      else:
            i, j = i + 1, j - 1
   return True

   
if __name__ == "__main__":
    
   print(valid_palindrome("A man, a plan, a canal: Panama"))