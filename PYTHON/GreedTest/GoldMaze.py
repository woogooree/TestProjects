def growRich() :
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = goldMaze[0][0]

    rowSum = memo[0][0]
    for i in range(1, ROW) :
        rowSum += goldMaze[0][i]
        memo[0][i] = rowSum

    colSum = memo[0][0]
    for i in range(1, COL) :
        colSum += goldMaze[i][0]
        memo[i][0] = colSum

    for row in range (1, ROW) :
        for col in range (1, COL) :
            if (memo[row][col-1] > memo[row-1][col]) :
                memo[row][col] = memo[row][col-1] + goldMaze[row][col]
            else :
                memo[row][col] = memo[row-1][col] + goldMaze[row][col]
    
    return memo[ROW-1][COL-1]
