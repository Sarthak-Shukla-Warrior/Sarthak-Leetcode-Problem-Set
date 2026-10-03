class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left=0
        right=0
        Max=0

        for i in range(0,len(s)):
            if(s[i]=='('):
                left+=1
            else:
                right+=1

            if(left==right):
                Max=max(Max,left*2)

            elif(right>left):
                left=right=0
            
            else:
                continue

        left=0
        right=0

        for i in range(len(s)-1,-1,-1):
            if(s[i]=='('):
                left+=1
            else:
                right+=1

            if(left==right):
                Max=max(Max,left*2)

            elif(left>right):
                left=right=0

            else:
                continue
        
        return Max