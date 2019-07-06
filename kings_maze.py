'''

The King's March
You’re given a chess board with dimension n x n. There’s a king at the bottom right square of the board marked with s.
The king needs to reach the top left square marked with e. 
The rest of the squares are labeled either with an integer p (marking a point) or with x marking an obstacle.
Note that the king can move up, left and up-left (diagonal) only.
Find the maximum points the king can collect and the number of such paths the king can take in order to do so.

Input Format
The first line of input consists of an integer t. This is the number of test cases.
Each test case contains a number n which denotes the size of board. 
This is followed by n lines each containing n space separated tokens.

Output Format
For each case, print in a separate line the maximum points that can be collected and
the number of paths available in order to ensure maximum, both values separated by a space.
If e is unreachable from s, print 0 0.

Sample Input
3
3
e 2 3
2 x 2
1 2 s
3
e 1 2
1 x 1
2 1 s
3
e 1 1
x x x
1 1 s

Sample Output
7 1
4 2
0 0

Constraints
1 <= t <= 100

2 <= n <= 200

1 <= p <= 9 

'''


def get_input():
   t = int(input())
   total_sol = []
   for _ in range(t):
      size = int(input())
      arr = [] 
      for i in range(size):
         arr.append(input().split()) 
      total_sol.append(arr)
   return total_sol 
total_sol = get_input()


def is_valid(row,  col, N, M, maze):
   if (row >=0 and row < N) and (col>=0 and col<M) and (maze[row][col]!='x'):return True 
   return False 


def solve_maze(maze, row,  col, N, M, path, visited, max_path):
   if (row == 0) and (col == 0):
      print ("reached destination", path)  
      tmp_sum = sum([int(maze[x][y]) for (x,y) in path if maze[x][y] not in ['s', 'x']])
      max_path.append(tmp_sum)
      path = []
      return 
   visited[row][col] = 1
   if is_valid(row, col, N, M, maze):
       #check left
       path.append([row, col]) 
       if (col-1 >= 0 and (not visited[row][col-1])): 
           solve_maze(maze, row, col-1, N, M, path, visited,max_path)
       #check up
       if (row-1 < N and (not visited[row-1][col])): 
          solve_maze(maze, row-1, col, N, M, path, visited, max_path)
       #check left-up
       if ((row-1 >=0 and col-1>=0) and (not visited[row-1][col-1])): 
          solve_maze(maze, row-1, col-1, N, M, path, visited, max_path)
       path.remove([row,col])  
   #print ("mark unvisited", [row,col])
   visited[row][col] = 0
   return    

def king_maze(maze, n, m): 
   start, end = n-1, m-1 
   path = []
   visited = [[0]*m for x in range(n)]
   max_path = []
   solve_maze(maze, start, end, n, m, path, visited, max_path)
    
   max_path.sort()
   tmp_dict  = {} 
   c = -1
   for each in max_path:
      if c < each:
         c  = each
      if not tmp_dict.get(str(each), 0):
         tmp_dict[str(each)] =0       
      tmp_dict[str(each)] = tmp_dict[str(each)]+1     
   if max_path:
      print (c, tmp_dict[str(c)])
   else:
      print (0,0)

for each in total_sol:
   king_maze(each, len(each), len(each))
   
   
#Thanks Pritam :)

