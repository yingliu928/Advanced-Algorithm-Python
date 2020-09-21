
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        List.sort(citations, reverse=True)
        i = len(citations) - 1
        while(i >= 0 and citations[i] < i):
            i -= 1

        return i


solution = Solution()
print(solution.hIndex([8, 7, 4, 3, 1]))
print(solution.hIndex([]))
print(solution.hIndex([0]))
