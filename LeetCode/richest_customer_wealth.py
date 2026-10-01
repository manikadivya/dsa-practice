class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        count = 0
        max_count = 0
        for i in accounts:
            for j in i:
                count = count+j
            max_count = max(max_count,count)
            count = 0
        return max_count
        