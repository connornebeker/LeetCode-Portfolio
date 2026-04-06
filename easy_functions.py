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

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
                
        return right
    # print(mySqrt(8))

    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        
        for char in s:
            if char == '(':
                if depth > 0:
                    result.append(char)
                depth += 1
            else:  
                if depth > 1:
                    result.append(char)
                depth -= 1
        
        return ''.join(result)
    # print(removeOuterParentheses("(()())(())(()(()))"))

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next        
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
    # print(isPalindrome([1,2,2,1]))