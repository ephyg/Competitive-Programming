class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dict={'r1':"qwertyuiop","r2":"asdfghjkl","r3":"zxcvbnm"}
        cont=[]
        for i in range(len(words)):
            word=words[i].lower()
            if(word[0] in dict['r1']):
                for j in range(0,len(words[i])):
                    if(word[j] in dict['r1']):
                        if(len(word)-1==j):
                            cont.append(words[i])
                        else:
                            continue
                    else:
                        break
            if(word[0] in dict['r2']):
                for j in range(0,len(words[i])):
                    if(word[j] in dict['r2']):
                        if(len(word)-1==j):
                            cont.append(words[i])
                        else:
                            continue
                    else:
                        break
                
            if(word[0] in dict['r3']):
                for j in range(0,len(words[i])):
                    if(word[j] in dict['r3']):
                        if(len(word)-1==j):
                            cont.append(words[i])
                        else:
                            continue
                    else:
                        break
                
        return cont
            
        