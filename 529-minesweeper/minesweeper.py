class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        r, c = click

        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        def countMines(x, y):
            count = 0
            for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "M":
                    count += 1
            return count

        def dfs(x, y):
            if board[x][y] != "E":
                return
            mines = countMines(x, y)
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = "B"
                for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        dfs(nx, ny)

        dfs(r, c)
        return board
