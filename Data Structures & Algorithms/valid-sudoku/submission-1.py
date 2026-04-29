
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
          for c in range(9):
            board_box = board[r][c]

            if board_box == ".":
              continue

            if (
              r in row[board_box] or c in col[board_box] or (r // 3, c // 3) in box[board_box]
            ):
              return False

            row[board_box].add(r)
            col[board_box].add(c)
            box[board_box].add((r // 3, c // 3))

        return True
