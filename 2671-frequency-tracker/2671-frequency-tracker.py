class FrequencyTracker:

    def __init__(self):
        self.nums=defaultdict(int)
        self.frequency_=defaultdict(int)

    def add(self, number: int) -> None:
        self.frequency_[self.nums[number]]-=1
        # self.freq[self.count[number]] -= 1
        self.nums[number]+=1
        self.frequency_[self.nums[number]]+=1
    def deleteOne(self, number: int) -> None:
        if(self.nums[number]>0):
            self.frequency_[self.nums[number]]-=1
            self.nums[number]-=1
            self.frequency_[self.nums[number]]+=1
        

    def hasFrequency(self, frequency: int) -> bool:
        if(self.frequency_[frequency]>0):
            return True
        else:
            return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)