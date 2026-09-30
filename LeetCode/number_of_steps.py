class Solution:
    def numberOfSteps(self, num: int) -> int:
        temp = num
        count = 0

        while temp > 0:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = temp - 1

            count += 1

        return count