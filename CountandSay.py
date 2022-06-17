class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        s=self.countAndSay(n-1)
        newString=""
        ch=s[0]
        count=1
        for i in range(len(s)):
            if s[i]!=ch:
                newString+=str(count)
                newString+=ch
                count=1
                ch=s[i]
            elif i!=0:
                count+=1
        newString+=str(count)
        newString+=ch
        return newString
            
            