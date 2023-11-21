class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter = 0
        mod = (10**9) + 7
        dics =collections.Counter()
        for num in nums:
            num -= int((str(num))[::-1])
            counter += dics[num]
            dics[num] += 1
        return counter % mod