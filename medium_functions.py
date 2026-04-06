class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        while num > 999:
            result += 'M'
            num -= 1000

        if num > 899:
            result += 'CM'
            num -= 900
        
        if num > 499:
            result += 'D'
            num -= 500

        if num > 399:
            result += 'CD'
            num -= 400

        while num > 99:
            result += 'C'
            num -= 100
            
        if num > 89:
            result += 'XC'
            num -= 90
        
        if num > 49:
            result += 'L'
            num -= 50

        if num > 39:
            result += 'XL'
            num -= 40

        while num > 9:
            result += 'X'
            num -= 10
        
        if num > 8:
            result += 'IX'
            num -= 9

        if num > 4:
            result += 'V'
            num -= 5
        
        if num > 3:
            result += 'IV'
            num -= 4
        
        while num > 0:
            result += 'I'
            num -= 1

        return result
    # print(intToRoman(1994))

    def maxArea(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            water = max(water, width * current_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return water
    # print(maxArea([1,8,6,2,5,4,8,3,7]))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        def is_valid_unit(unit: List[str]) -> bool:
            nums = [x for x in unit if x != '.']
            return len(nums) == len(set(nums))

        for row in board:
            if not is_valid_unit(row):
                return False

        for col in zip(*board):
            if not is_valid_unit(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not is_valid_unit(box):
                    return False
        
        return True
    # print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []
    
        for i, char in enumerate(expression):
            if char in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l + r)
                        elif char == '-':
                            results.append(l - r)
                        elif char == '*':
                            results.append(l * r)
        
        if not results:
            results.append(int(expression))
        
        return results
    # print(diffWaysToCompute("2*3-4*5"))

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
    # print(insertIntoBST([4,2,7,1,3], 5))