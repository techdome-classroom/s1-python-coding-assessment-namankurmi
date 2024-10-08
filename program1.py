class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(i, j):
            # Base case: Stop DFS if out of bounds or in water
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 'W':
                return
            # Mark the current cell as visited by changing it to water
            grid[i][j] = 'W'
            # Explore all four directions (up, down, left, right)
            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i, j + 1)  # Right

        # Traverse the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':  # Found an unvisited land cell
                    island_count += 1  # New island found
                    dfs(i, j)  # Perform DFS to mark the entire island

        return island_count
