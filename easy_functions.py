class Solution:
    def isPalindrome(x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if x == y:
            return True
        else:
            return False
    # print(isPalindrome(12321))

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
    # print(removeElement([3,2,2,3], 3))

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
           
        return k
    # print(removeDuplicates([1,1,2]))

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
            
        return []
    # print(twoSum([2,7,11,15], 9))