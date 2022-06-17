class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)==len(needle) and needle==haystack:
            return 0
        if len(haystack)<len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                if (i+len(needle)<=len(haystack) or len(needle)==1) and haystack[i:i+len(needle)]==needle:
                    return i
        return -1
        
        