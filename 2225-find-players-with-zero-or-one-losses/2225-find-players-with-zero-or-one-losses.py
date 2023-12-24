class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=[]
        loser=[]
        for i in range(len(matches)):
            winner.append(matches[i][0])
            loser.append(matches[i][1])   
        players=list(set(winner+loser))
        dict=Counter(loser)
        not_lose=[]
        lost_ones=[]
        
        for i in range(len(players)):
            if(players[i] not in dict):
                not_lose.append(players[i])
            else:
                if(dict[players[i]]==1):
                    lost_ones.append(players[i])
        not_lose.sort()
        lost_ones.sort()
        return [not_lose,lost_ones]
                