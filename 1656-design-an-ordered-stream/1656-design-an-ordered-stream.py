class OrderedStream:

    def __init__(self, n: int):
        self.strings=[0]*n
        self.start=0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.strings[idKey-1]=value
        answer=[]
        while self.start <len(self.strings) and self.strings[self.start]!=0:
            answer.append(self.strings[self.start])
            self.start+=1
        return answer
      
                
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)