class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = set()
        for i in range(n):
            ptr_left = i + 1
            ptr_right = n - 1
            while ptr_left < ptr_right:
                if (nums[i], nums[ptr_left], nums[ptr_right]) not in result:
                    if nums[ptr_left] + nums[ptr_right] >  nums[i]*-1:
                        ptr_right -= 1
                    elif nums[ptr_left] + nums[ptr_right] <  nums[i]*-1:
                        ptr_left += 1
                    else:
                        result.add((nums[i], nums[ptr_left], nums[ptr_right]))
                        ptr_left +=1
                else:
                    ptr_left +=1
        return list(result)
            
            
