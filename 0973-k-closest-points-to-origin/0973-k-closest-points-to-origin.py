class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict=defaultdict(list)
        for i in range(len(points)):
            calc=(points[i][0])**2 + (points[i][1])**2
            dict[calc].append([points[i][0],points[i][1]])
        key=sorted(list(dict.keys()))
        ans=[]
        i=0
        while len(ans)!=k:
            for elem in dict[key[i]]:
                ans.append(elem)
            i+=1
        return ans