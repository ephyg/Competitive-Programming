class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ls=[i[0] for i in paths]
        for i in range(len(paths)):
            if not (paths[i][1] in ls ):
                return paths[i][1]
        