#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        # House Robber 1 solution
        def helper(nums):
            rob1, rob2 = 0, 0
            
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


# @lc code=end

