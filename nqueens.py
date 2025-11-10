class NQBacktracking:
    def __init__(self, x_, y_):
        self.ld = [0] * 30      # left diagonal
        self.rd = [0] * 30      # right diagonal
        self.cl = [0] * 30      # column tracker
        self.x, self.y = x_, y_ # initial queen position

    def printSolution(self, board):
        print("\nN-Queen Backtracking Solution")
        print(f"Initial queen at row = {self.x}, column = {self.y}\n")
        for row in board:
            print(" ".join(map(str, row)))

    def solveNQUtil(self, board, col):
        # If all queens placed
        if col >= N:
            return True
        
        # Skip initial fixed queen column
        if col == self.y:
            return self.solveNQUtil(board, col + 1)

        for i in range(N):
            # Skip initial fixed queen row
            if i == self.x:
                continue
            
            if (self.ld[i - col + N - 1] != 1 and
                self.rd[i + col] != 1 and
                self.cl[i] != 1):

                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1

                if self.solveNQUtil(board, col + 1):
                    return True

                # Backtrack
                board[i][col] = 0
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0
        
        return False

    def solveNQ(self):
        board = [[0]*N for _ in range(N)]

        # Place given queen
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1

        if not self.solveNQUtil(board, 0):
            print("No solution exists for this fixed queen position.")
            return False
        
        self.printSolution(board)
        return True


# Driver Code
if __name__ == "__main__":
    N = 8              # Chessboard Size
    x, y = 3, 2        # Fixed queen at row 3, column 2 (0-indexed)

    NQ = NQBacktracking(x, y)
    NQ.solveNQ()
