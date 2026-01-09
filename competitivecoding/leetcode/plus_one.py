figits=[2,9,9,9]
for i in range(len(figits)):
    if i==len(figits)-1:
        figits[i]=figits[i]+1
        if figits[i]>9:
            figits[i]=0
            figits[i-1]=figits[i-1]+1
            if figits[i-1]>=9:
                figits[i-1]=0
                figits[i-2]=figits[i-2]+1
                if figits[i-2]>=9:
                    figits[i-2]=0
                    figits[i-3]=figits[i-3]+1
        
print(figits) 


#actual solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: # type: ignore
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits