class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=i
        
        for i in range(len(operations)):
            nums[dict[operations[i][0]]] = operations[i][1]
            dict[operations[i][1]]=dict[operations[i][0]]
            dict.pop(operations[i][0])
            
        return nums