class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
            dict={}
            for i in range(len(paths)):
                splited=[i for i in paths[i].split()]
                for i in range(1,len(splited)):
                    open_bracket=splited[i].index('(')
                    close_bracket=splited[i].index(')')
                    key=splited[i][open_bracket+1:close_bracket]
                    value=f"{splited[0]}/{splited[i][0:open_bracket]}"
                    if key in dict:
                        dict[key].append(value)
                    else:
                        dict[key]=[value]
            return [dict[i] for i in dict if(len(dict[i])>1)]

            