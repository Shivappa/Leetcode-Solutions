// Runtime: 933 ms (Top 28.58%) | Memory: 15.5 MB (Top 24.40%)
class Solution:
    def totalHammingDistance(self, arr: List[int]) -> int:

        total = 0
        for i in range(0,31):
            count = 0
            for j in arr :
                count+= (j >> i) & 1
            total += count*(len(arr)-count)
        return total