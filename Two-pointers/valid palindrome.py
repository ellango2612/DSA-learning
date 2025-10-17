'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
'''

# we should have 2 pointers, 1 at the beginning and the other at the end of the string. Then, we slide the 2 pointers at the same rate and compare the chars pointed too
# if they differ return false
# 11:28

## we need a func to check if the chars being compared are alphanumeric


class Solution:
    def isPalindrome(self, str):
        # def alphaNum(s):
        #     return ('A' <= s <= 'Z') or ('a' <= s <= 'z') or ('0' <= s <= '9')
        i = 0
        j = len(str)-1
        while i < j: # need to consider if str(i) or str(j) is alphanum
            while i < j and not str[j].isalnum():
                j-=1
            while i < j and not str[i].isalnum():
                i+=1
            if str[i].lower() == str[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
    
    # Time: O(n)
    # Space: O(1)
    