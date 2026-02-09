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
        curr = 0

        for i in range(len(height)):
            for j in range(len(height)):
                if height[j] > height[i]:
                    max_height = height[i]
                else:
                    max_height = height[j]
                curr = (j - i)*(max_height)
                if curr > water:
                    water = curr
        
        return water
    # print(maxArea([1,8,6,2,5,4,8,3,7]))