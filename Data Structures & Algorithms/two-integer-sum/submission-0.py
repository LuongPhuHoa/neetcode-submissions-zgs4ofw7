class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(0,n):
        #     for j in range(n-1,i,-1):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        indices = {}
        for i in range(0,n):
            if (target - nums[i]) in indices:
                return[indices[target - nums[i]],i]
            indices[nums[i]] = i
        return []
