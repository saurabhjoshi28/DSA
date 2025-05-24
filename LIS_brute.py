class Solution:
    def func(self,i,prev,nums):
        n=len(nums)
        if i==n:
            return 0
        pick=float('-inf')
        if prev==-1 or nums[prev]<nums[i]:
            pick=1+self.func(i+1,i,nums)
        notpick=0+self.func(i+1,prev,nums)
        return max(pick,notpick)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1-> brute force--> generate all subsequences(recursion) 
        # --> then of all subsequences only take the strictly increaing ones
        # ----->how will i know if a subsequence is strictly increasing?
        # ---------->ans= if the last element is smaller than the new.
        # --> take a variable and keep finding length of of new susequences
        # --> update our variable if we find a longer subsequence
        return self.func(0,-1,nums) # this function represents LIS