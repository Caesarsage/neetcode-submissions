
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
      rows = {}
      cols = {}
      sub_box = {}

      for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == ".":
                continue

            # initialize empty set so we can safely append to it
            # a simpler way is to use defaultdict(set)
            if r not in rows:
                rows[r] = set()
            
            if c not in cols:
                cols[c] = set()

            box = (r//3, c//3)
            if box not in sub_box:
                sub_box[box] = set()

            # now the main check for duplicates
            if val in rows[r] or val in cols[c] or val in sub_box[box]:
                return False


            cols[c].add(val)
            rows[r].add(val)
            sub_box[box].add(val)
        

      return  True