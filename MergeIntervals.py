class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        p = sorted(intervals, key=lambda x: x[0])
        ans = [p[0]]
        for i in range(1,len(p)):
            if ans[-1][1] >= p[i][0]:
                ans[-1][1] = max(ans[-1][-1],p[i][1])
            else:
                ans.append(p[i])
        return ans
