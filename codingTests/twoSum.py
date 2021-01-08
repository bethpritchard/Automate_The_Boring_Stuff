class TwoSum:
    @staticmethod
    def twoSum(nums, target):
        ans = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i not in ans and j not in ans:
                    ans.append(i)
                    ans.append(j)
        return ans



print(TwoSum.twoSum([3,2,4], 6));