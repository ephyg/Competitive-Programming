class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited=[[0,0]]
        x=0
        y=0
        for i in range(len(path)):
            if(path[i]=="N"):
                y+=1
            if(path[i]=="S"):
                y-=1
            if(path[i]=="E"):
                x+=1
            if(path[i]=="W"):
                x-=1
            if([x,y] in visited):
                return True
            visited.append([x,y])
        return False
                