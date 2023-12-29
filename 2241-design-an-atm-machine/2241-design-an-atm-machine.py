class ATM:

    def __init__(self):
        self.bank_amount=[0,0,0,0,0]
        self.bank_notes=[20,50,100,200,500]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.bank_amount[i]+=banknotesCount[i]
    def withdraw(self, amount: int) -> List[int]:
        answer=[0]*5
        for i in range(4,-1,-1):
            x=amount // self.bank_notes[i]
            n=min(x,self.bank_amount[i])
            amount-=(n*self.bank_notes[i])
            answer[i]+=n
        if(amount==0):
            for i in range(5):
                self.bank_amount[i]-=answer[i]
            return answer
        else:
            return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)