#
# https://developers.google.com/optimization/cp/queens
#
def nQueens(n):
    c=ChessBoard(n)
    DFS(c,0)
    return c.solutions
       
def DFS(CB, col):
    f=False
    for row in range(len(CB.board)):
        #CB.printBoard()
        if CB.isSafe(col, row):
            f=True
            CB.board[row][col]=1
            if col+1<len(CB.board):
                DFS(CB, col+1)
            else:
                CB.saveSolution()
        if f:
            CB.board[row][col]=0
            f=False
            
class ChessBoard:
    def __init__(self, n):       
        self.board=[]
        for i in range(n):
            self.board.append([0]*n)
        self.solutions=[]

    def isSafe(self, x, y):
        ln=len(self.board)
        # check if Q is visible from location
        for i in range(ln):
            d1,d2=x-y+i,x+y-i
            #   Horizontal          Vertical            Diagonals:   TL->BR                             TR->BL
            if self.board[y][i] or self.board[i][x] or (0<=d1<ln and self.board[i][d1]) or (0<=d2<ln and self.board[i][d2]):
                return 0
        return 1
            
    def saveSolution(self):
        sol=[0]*len(self.board)
        for i,e in enumerate(self.board):
            for j,k in enumerate(e):
                if k:
                    sol[j]=i+1
        self.solutions.append(sol)
    
    def printBoard(self):
        for e in self.board:
            print(e)
    
