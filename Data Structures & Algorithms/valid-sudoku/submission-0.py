class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = defaultdict(set)
        col_count = defaultdict(set)
        boxes_count = defaultdict(set)

        for r in range(9):
            for c in range(9):
                box = board[r][c]
                if box == ".":
                    continue
                
                if box in row_count[r] or box in col_count[c] or box in boxes_count[(r // 3, c // 3)]:
                    
                    return False
                col_count[c].add(box)
                row_count[r].add(box)
                boxes_count[(r//3, c//3)].add(box)

        return True


            