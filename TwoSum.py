class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        #Brute Force 暴力破解
        lenth = len(nums)
        for i in range(0,lenth ):
            for j in range(i + 1,lenth ):
                if nums[i]+nums[j] == target:
                    return [i,j]
                    '''
        #One-pass Hash Table 一次循环
        record = {}
        for i,present_num in enumerate(nums):
            remaining = target - present_num
            if remaining in record:
                return [record[remaining],i]
            record[present_num] = i
        return []

        # Two-pass Hash Table :第一次循环，把所有数存进字典，
        # 第二次循环，将target减去当前得到一个数，看看该数是否在字典的键中，如果有，返回


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums,target))