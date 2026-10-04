class Solution:
    def checkValidString(self, s: str) -> bool:
        hb=0
        lb=0

        for ch in s:
            if(ch=="("):
                hb+=1
                lb+=1

            elif(ch=="*"):
                hb+=1
                lb-=1
                if(lb<0):
                    lb=0

            else:
                hb-=1
                lb-=1
                if(hb<0):
                    return False
                if(lb<0):
                    lb=0

        return lb==0