```
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(row, col, track):
            if col in track:
                return False
            for k in range(row):
                if row + col == k + track[k] or row - col == k - track[k]:
                    return False
            return True
            
        def backtrack(row, track):
            if row == n:
                res.append(track)
                return 
            for col in range(n):
                if valid(row, col, track):
                    backtrack(row+1, track+[col])
        res = []
        backtrack(0, [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in l] for l in res]
```
