class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b=0
        c=0
        l1=[]
        l2=[]
        
        for i in secret:
            l1.append(i)
            
        for j in guess:
            l2.append(j)
        
        for i in range (len(secret)):
            if( secret[i]==guess[i] ):
                b+=1
                l1.remove(secret[i])
                l2.remove(guess[i])
        for i in l1:
            if(i in l2):
                c+=1
                l2.remove(i)
        b=str(b)
        c=str(c)
        return b+"A"+c+"B"
        
        