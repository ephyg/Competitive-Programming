class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        for i in range(1,len(words)):
            min_len=min(len(words[i-1]),len(words[i]))
            for j in range(min_len):
                p=order.index(words[i-1][j])
                q=order.index(words[i][j])
                print(p,q)
                if (q>p):
                    break
                elif(p>q):
                    return False
                else:
                    if(min_len-1==j):
                        if(len(words[i])<len(words[i-1])):
                            return False
                
        return True
                            
            