class Bitset:

    def __init__(self, size: int):
        self.bitset=[0]*size
        self.rev_bitset=[1]*size
        self.ones=0
        self.zeros=size
    def fix(self, idx: int) -> None:
        if not self.bitset[idx]:
            self.bitset[idx]=1
            self.rev_bitset[idx]=0
            self.ones+=1
            self.zeros-=1

    def unfix(self, idx: int) -> None:
        if self.bitset[idx]:
            self.bitset[idx]=0
            self.rev_bitset[idx]=1
            self.ones-=1
            self.zeros+=1

    def flip(self) -> None:
        self.bitset,self.rev_bitset=self.rev_bitset,self.bitset
        self.ones,self.zeros=self.zeros,self.ones
    def all(self) -> bool:
        return self.ones==len(self.bitset)
        

    def one(self) -> bool:
        return self.ones>=1

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        s=""
        for i in range(len(self.bitset)):
            s+=str(self.bitset[i])
        return s
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()