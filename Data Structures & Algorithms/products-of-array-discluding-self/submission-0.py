class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            temp = 1
            for j in range(n):
                if i != j:
                    temp = temp * nums[j]
            result.append(temp)
        return result
