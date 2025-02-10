class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        for i in s.lower():
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                list1.append(i)  

        left = 0
        right = len(list1) - 1
        while left < right:
            if list1[left] != list1[right]:
                return False
            left += 1
            right -= 1
        return True   
                         
        #return list1 == list1[::-1]    