# Q28: Implement strStr() -- https://leetcode.com/problems/implement-strstr/
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1: Input --> haystack = "hello", needle = "ll" -- Ouput --> 2

class Solution():
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        first_index = 0
        while i <= len(haystack):
            if len(needle) > len(haystack):
                first_index =- 1
            elif needle == "":
                first_index = 0
                break
            elif needle == haystack[i:i+len(needle)]:
                first_index = i
                break
            elif needle != haystack and i == len(haystack) - len(needle):
                first_index = -1
                break
            i += 1
        return first_index

haystack = 'aaa'
needle = 'a'
print(Solution().strStr(haystack=haystack, needle=needle))