def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    queens = []

    def dfs(row):
        if row == n:
            solutions.append(queens.copy())
            return

        for col in range(n):
            valid = True

            for prev_row in range(row):
                prev_col = queens[prev_row]

                # Check column and diagonal conflicts
                if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                    valid = False
                    break

            if valid:
                queens.append(col)
                dfs(row + 1)
                queens.pop()

    dfs(0)
    return solutions