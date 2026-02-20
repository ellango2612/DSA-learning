def maxArea(grid):
    # edge case
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    maxArea = 0

    def dfs(r,c):
        area = 1
        visited.add((r,c))
        for nr,nc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]==1:
                area += dfs(nr,nc)
        return area
    
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in visited and grid[r][c] == 1:
                maxArea = max(maxArea, dfs(r,c))
    return maxArea

def test_basic_cases():
    tests = [
        # empty grid
        ([], 0),

        # all water
        ([[0,0],[0,0]], 0),

        # single land
        ([[1]], 1),

        # simple island
        ([[1,1],
          [1,1]], 4),

        # multiple islands
        ([[1,0,0,1],
          [1,0,0,1],
          [0,0,1,0]], 2),

        # long horizontal
        ([[1,1,1,1,1]], 5),

        # long vertical
        ([[1],[1],[1],[1]], 4),

        # diagonal not connected
        ([[1,0],
          [0,1]], 1),
    ]

    for i, (grid, expected) in enumerate(tests):
        result = maxArea(grid)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"

    print("Basic tests passed ✅")

if __name__ == "__main__":
    test_basic_cases()