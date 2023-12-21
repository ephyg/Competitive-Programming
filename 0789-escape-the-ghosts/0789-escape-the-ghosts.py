class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        me=abs(target[0])+abs(target[1])
        for i in range(len(ghosts)):
            x=abs(ghosts[i][0]-target[0])
            y=abs(ghosts[i][1]-target[1])            
            if((x+y)<=me):
                return False
        return True
                